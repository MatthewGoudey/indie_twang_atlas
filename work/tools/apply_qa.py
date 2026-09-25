#!/usr/bin/env python3
"""Apply QA results (qa/result_*.jsonl) to staging files AND master.jsonl (IDs preserved).
- ok/fix with an independent new_source: add the source (max 3), confidence High if >=2 sources.
- fix: apply corrected fields (album, year, label, type, key_tracks).
- fail: turn the staging row into a needs_verification line; drop from master.
Writes qa/applied.jsonl (log) and appends a summary to qa_log.jsonl."""
import json, glob, os, re, unicodedata, collections, datetime
W = "/home/claude/work"; os.chdir(W)
def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower().replace("&", "and")
    s = re.sub(r"^the\s+", "", s); return re.sub(r"[^a-z0-9]", "", s)
master = [json.loads(l) for l in open("master.jsonl")]
byid = {r["id"]: r for r in master}
results = {}
for f in sorted(glob.glob("qa/result_*.jsonl")):
    for l in open(f):
        try: q = json.loads(l)
        except Exception: continue
        if q.get("id") in byid: results[q["id"]] = q
already = set()
if os.path.exists("qa/applied.jsonl"):
    already = {json.loads(l)["id"] for l in open("qa/applied.jsonl")}
todo = {k: v for k, v in results.items() if k not in already}
# index staging rows by key
files = sorted(glob.glob("staging/lane_*.jsonl"))
stag = {f: [l for l in open(f, encoding="utf-8")] for f in files}
changed = set()
def key(a, b): return (norm(a), norm(b))
cnt = collections.Counter(); log = []
for qid, q in todo.items():
    m = byid[qid]; k = key(m["artist"], m["album"]); v = q.get("verdict"); cnt[v] += 1
    c = q.get("corrections") or {}
    def patch(r):
        if v == "fix":
            for fld in ("album", "year", "label", "type", "key_tracks"):
                if fld in c and c[fld] not in (None, "", []):
                    if fld == "year":
                        try: r[fld] = int(c[fld])
                        except Exception: continue
                    else: r[fld] = c[fld]
        ns = q.get("new_source") or ""
        if v in ("ok", "fix") and ns.startswith("http") and ns not in r["sources"]:
            r["sources"] = (r["sources"] + [ns])[:3]
        if v in ("ok", "fix") and q.get("independent") and len(r["sources"]) >= 2:
            r["confidence"] = "High"
        return r
    hit = False
    for f, lines in stag.items():
        for i, l in enumerate(lines):
            if not l.strip(): continue
            r = json.loads(l)
            if r.get("needs_verification") or key(r["artist"], r["album"]) != k: continue
            if v == "fail":
                nvr = {"needs_verification": True, "artist": r["artist"], "album": r["album"], "year": r.get("year", 0),
                       "note": "QA re-check failed: " + (q.get("note") or "")[:300]}
                lines[i] = json.dumps(nvr, ensure_ascii=False) + "\n"
            elif v in ("ok", "fix"):
                lines[i] = json.dumps(patch(r), ensure_ascii=False) + "\n"
            hit = True; changed.add(f)
    if v == "fail":
        master = [r for r in master if r["id"] != qid]
    elif v in ("ok", "fix"):
        patch(m)
    log.append({"id": qid, "verdict": v, "applied_to_staging": hit, "corrections": c})
for f in changed:
    open(f, "w", encoding="utf-8").writelines(stag[f])
with open("master.jsonl", "w") as fo:
    for r in master: fo.write(json.dumps(r, ensure_ascii=False) + "\n")
with open("qa/applied.jsonl", "a") as fo:
    for e in log: fo.write(json.dumps(e, ensure_ascii=False) + "\n")
print(dict(cnt), "applied", len(log), "not found in staging:", sum(1 for e in log if not e["applied_to_staging"]))
