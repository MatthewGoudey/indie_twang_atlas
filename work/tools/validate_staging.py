#!/usr/bin/env python3
"""Validate a staging JSONL file against the Albums schema and controlled vocabularies.
Usage: python3 validate_staging.py path/to/file.jsonl  [--quiet]
Prints problems per line; prints OK when clean. Exit code 1 if problems."""
import json, sys, re, os

ROOT = "/home/claude/work"
vocab = json.load(open(os.path.join(ROOT, "skeleton/vocab.json")))
lanes = {l["id"]: l for l in json.load(open(os.path.join(ROOT, "skeleton/lanes.json")))}
TAGS = set(vocab["tags"]); STYLES = set(vocab["styles"]); REGIONS = set(vocab["regions"])
TYPES = set(vocab["types"]); PRI = set(vocab["priority"]); LB = set(vocab["lineage_basis"]); CONF = set(vocab["confidence"])
REQ = ["artist","album","year","type","label","primary_lane","secondary_lanes","style","region","base","scene",
       "descriptors","description","lineage","lineage_basis","key_tracks","priority","start_here","terry","sources","confidence","borderline_note"]

def layer(y):
    if y >= 2014: return "L1"
    if y >= 1998: return "L2"
    if y >= 1987: return "L3"
    if y >= 1978: return "L4"
    if y >= 1965: return "L5"
    return "L6"

def check(path, quiet=False):
    problems = []; n = 0; nv = 0; seen = {}
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line: continue
            try:
                r = json.loads(line)
            except Exception as e:
                problems.append(f"line {i}: invalid JSON ({e})"); continue
            if r.get("needs_verification"):
                nv += 1
                if not r.get("artist") or not r.get("album"): problems.append(f"line {i}: needs_verification entry missing artist/album")
                continue
            n += 1
            p = lambda msg: problems.append(f"line {i} [{r.get('artist','?')} — {r.get('album','?')}]: {msg}")
            for k in REQ:
                if k not in r: p(f"missing field '{k}'")
            if problems and problems[-1].startswith(f"line {i}") and "missing field" in problems[-1]:
                pass
            y = r.get("year")
            if not isinstance(y, int) or y < 1920 or y > 2026: p(f"bad year {y!r}")
            if r.get("type") not in TYPES: p(f"bad type {r.get('type')!r}")
            if not r.get("label"): p("empty label")
            pl = r.get("primary_lane")
            if pl not in lanes: p(f"unknown primary_lane {pl!r}")
            sl = r.get("secondary_lanes", [])
            if not isinstance(sl, list) or len(sl) > 2 or any(s not in lanes for s in sl): p(f"bad secondary_lanes {sl!r}")
            if pl in sl: p("primary lane repeated in secondary_lanes")
            if r.get("style") not in STYLES: p(f"bad style {r.get('style')!r}")
            if r.get("region") not in REGIONS: p(f"bad region {r.get('region')!r}")
            d = r.get("descriptors", [])
            if not isinstance(d, list) or not (3 <= len(d) <= 6): p(f"descriptors must be a list of 3–6 tags (got {len(d) if isinstance(d,list) else d})")
            else:
                bad = [t for t in d if t not in TAGS]
                if bad: p(f"unknown descriptors {bad}")
            desc = r.get("description", "")
            sc = len(re.findall(r"[.!?](\s|$)", desc))
            if len(desc) < 120: p(f"description too short ({len(desc)} chars)")
            if sc > 5: p(f"description has {sc} sentences (max 4)")
            if re.search(r'"[^"]{60,}"', desc): p("description contains a long quote (>10 words)")
            if not r.get("lineage") or len(r.get("lineage","")) < 40: p("lineage missing/too short")
            if r.get("lineage_basis") not in LB: p(f"bad lineage_basis {r.get('lineage_basis')!r}")
            kt = r.get("key_tracks", [])
            if not isinstance(kt, list) or not (1 <= len(kt) <= 3): p("key_tracks must be a list of 1–3")
            if r.get("priority") not in PRI: p(f"bad priority {r.get('priority')!r}")
            if r.get("start_here") not in ("Y", ""): p("start_here must be 'Y' or ''")
            t = r.get("terry", "")
            if t and not t.startswith("https://www.noexpectations.fyi/"): p(f"terry must be a noexpectations.fyi URL or '' (got {t})")
            s = r.get("sources", [])
            if not isinstance(s, list) or not (1 <= len(s) <= 3) or any(not str(u).startswith("http") for u in s): p("sources must be 1–3 http URLs")
            if r.get("confidence") not in CONF: p(f"bad confidence {r.get('confidence')!r}")
            if r.get("confidence") == "High" and isinstance(s, list) and len(s) < 2: p("High confidence needs 2 sources")
            key = (re.sub(r"\W+", "", str(r.get("artist","")).lower()), re.sub(r"\W+", "", str(r.get("album","")).lower()))
            if key in seen: p(f"duplicate of line {seen[key]}")
            seen[key] = i
    if not quiet:
        for pr in problems: print(pr)
    print(f"{n} rows, {nv} needs_verification, {len(problems)} problems")
    if not problems: print("OK")
    return problems

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    quiet = "--quiet" in sys.argv
    allp = []
    for a in args:
        allp += check(a, quiet)
    sys.exit(1 if allp else 0)
