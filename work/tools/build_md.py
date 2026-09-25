#!/usr/bin/env python3
"""Build V_Map.md (Markdown source for the V Map) from master.jsonl, essays/*.json and sheets/*.json.
Figures are referenced relative to the .md file (figs/...). Convert with tools/md_to_pdf.py.
Usage: python3 build_md.py [out_dir]   (default: work/deliverables)"""
import json, os, re, sys, shutil, collections

W = "/home/claude/work"
OUT = sys.argv[1] if len(sys.argv) > 1 else f"{W}/deliverables"
rows = [json.loads(l) for l in open(f"{W}/master.jsonl")]
by_id = {r["id"]: r for r in rows}
lanes = json.load(open(f"{W}/skeleton/lanes.json"))
L = {l["id"]: l for l in lanes}
def js(p, d=None):
    p = f"{W}/{p}"
    return json.load(open(p)) if os.path.exists(p) else d
scenes = js("sheets/scenes.json", [])
labels = js("sheets/labels.json", [])
paths = js("sheets/paths.json", [])
cited, missing = set(), set()

def ref(text):
    """Validate [A0123] references; keep them as `A0123` code spans."""
    def sub(m):
        i = m.group(1); cited.add(i)
        if i not in by_id: missing.add(i)
        return f"`{i}`"
    return re.sub(r"\[(A\d{4})\]", sub, text)

def album(i):
    cited.add(i)
    r = by_id.get(i)
    if not r: missing.add(i); return f"[missing {i}]"
    return f"{r['artist']} – *{r['album']}* ({r['year']}) `{i}`"

def essay(name):
    return js(f"essays/{name}.json")

out = []
w = out.append
n_alb = len(rows)
w("---\ntitle: \"The V\"\nsubtitle: \"A map of indie twang, slacker rock, and everything that fed them\"\n"
  f"description: \"Companion to V_Album_Atlas.xlsx · {n_alb:,} albums · 54 lanes\"\n---\n")
w("# The V\n\n*A map of indie twang, slacker rock, and everything that fed them*\n")
w(f"Companion to **V_Album_Atlas.xlsx** · {n_alb:,} albums · 54 lanes\n")
w("## Contents\n")
for t, d in [("1. How to read this", "layers, zones, how to use the map with the spreadsheet"),
             ("2. The V diagram", "every lane, and the eight trunk lines"),
             ("3. The bottom of the V", "the nine Core lanes, C1–C9"),
             ("4. Climbing the V", "the V lanes, layer by layer, and the roots lane R1"),
             ("5. Off the edges", "the fourteen Context lanes, X1–X14"),
             ("6. Scenes and labels", "gazetteer"),
             ("7. Listening paths", "routes from the anchors to the top of the V"),
             ("8. Appendix", "the borderline decisions that shaped the map")]:
    w(f"- **{t}** — {d}")
w("")

# 1
w('<div class="pagebreak"></div>\n\n# 1. How to read this\n')
for p in (essay("intro") or {}).get("paragraphs", []): w(ref(p) + "\n")
w("## Layers and zones\n")
cnt = collections.Counter((r["layer"], r["zone"]) for r in rows)
w("| Layer | Years | Core | V | Context |\n|---|---|---:|---:|---:|")
for ly, nm, yrs in [("L1", "Now", "2014–2026"), ("L2", "Bridge", "1998–2013"), ("L3", "Nineties", "1987–1997"),
                    ("L4", "Underground", "1978–1986"), ("L5", "Classic", "1965–1977"), ("L6", "Roots", "before 1965")]:
    w(f"| {ly} {nm} | {yrs} | {cnt[(ly,'Core')]} | {cnt[(ly,'V')]} | {cnt[(ly,'Context')]} |")
w("")
w("| Zone | What it means | Depth |\n|---|---|---|\n| Core | The bottom of the V: the scenes happening now (C1–C9) | Completionist |\n"
  "| V | Direct ancestors and close siblings of the Core (V1–V30, plus the roots lane R1) | Deep |\n"
  "| Context | Popular branches whose main line leads outside the V (X1–X14) | Landmarks only |\n")
w("Album IDs such as `A0001` refer to rows on the Albums sheet of V_Album_Atlas.xlsx; filter the sheet by ID, lane or artist for the full entry, descriptors, key tracks and sources.\n")

# 2
w('<div class="pagebreak"></div>\n\n# 2. The V diagram\n')
w("The chart shows every lane as a box, placed in the layer where it is centred and coloured by zone (orange Core, blue V, grey Context). Arrows run from parent to child: from what fed a sound to what it fed. Dashed arrows touch a Context lane.\n")
w('<div class="landscape"><img src="figs/v_lineage.png" alt="The V: lineage of every lane"></div>\n')
w("## The eight trunk lines\n")
w("![The eight trunk lines](figs/trunk_lines.png)\n")
w("Each trunk line is one of the eight routes by which an older sound reaches the Core: (1) Neil Young & Crazy Horse guitar; (2) country played by punk and indie kids; (3) deadpan, funny-sad songwriting; (4) Southern storytelling rock; (5) slow, sad and noisy textures; (6) the DIY network; (7) Cosmic American Music; (8) folk songwriting.\n")

def lane_section(i, level):
    l = L[i]; e = essay(i)
    n = sum(1 for r in rows if r["primary_lane"] == i)
    w(f"{'#' * level} {i} · {l['name']}\n")
    w(f"*{l['zone']} zone · main era {l['era']} · {n} albums in the atlas · fed by {', '.join(l['parents']) or '—'}*\n")
    if not e: w(f"*[Essay pending for {i}.]*\n"); return
    for p in e["paragraphs"]: w(ref(p) + "\n")
    if e.get("essentials"):
        w(f"**{e.get('essentials_label', 'Essential albums')}**\n")
        for x in e["essentials"]:
            w(f"- {album(x['id'])}" + (f" — {ref(x['note'])}" if x.get("note") else ""))
        w("")

# 3
w('<div class="pagebreak"></div>\n\n# 3. The bottom of the V: the Core lanes\n')
for p in (essay("core_intro") or {}).get("paragraphs", []): w(ref(p) + "\n")
for i in ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]: lane_section(i, 2)

# 4
w('<div class="pagebreak"></div>\n\n# 4. Climbing the V\n')
for p in (essay("climb_intro") or {}).get("paragraphs", []): w(ref(p) + "\n")
for title, ids in [("L1–L2 · The bridge and the siblings (1996–now)", ["V1", "V2", "V3", "V4", "V5", "V6", "V7"]),
                   ("L3 · The Nineties (1987–1997)", ["V9", "V10", "V11", "V12", "V13"]),
                   ("L4 · The Underground (1978–1986)", ["V14", "V15", "V16", "V17", "V18", "V19"]),
                   ("L5 · The Classic era (1965–1977)", ["V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "V29", "V30", "V8"]),
                   ("L6 · Roots (before 1965)", ["R1"])]:
    w(f"## {title}\n")
    for i in ids: lane_section(i, 3)

# 5
w('<div class="pagebreak"></div>\n\n# 5. Off the edges: the Context lanes\n')
for p in (essay("context_intro") or {}).get("paragraphs", []): w(ref(p) + "\n")
for k in range(1, 15): lane_section(f"X{k}", 3)

# 6
w('<div class="pagebreak"></div>\n\n# 6. Scenes and labels\n\n## Scenes\n')
for s in scenes:
    n = sum(1 for r in rows if r.get("scene") == s["scene"])
    extra = f" · {n} albums tagged" if n else ""
    lab = f" Labels: {s['key_labels']}." if s.get("key_labels") else ""
    w(f"**{s['scene']}** · {s['place']} · {s['years']}{extra}. {s['note']} Key artists: {s['key_artists']}.{lab}\n")
w("## Labels\n")
for l in labels:
    meta = " · ".join(x for x in [l.get("base", ""), l.get("years_active", "")] if x)
    w(f"**{l['label']}**" + (f" · {meta}" if meta else "") + f". {l['why']}\n")

# 7
w('<div class="pagebreak"></div>\n\n# 7. Listening paths\n')
for p in (essay("paths_intro") or {}).get("paragraphs", []): w(ref(p) + "\n")
for k, p in enumerate(paths, 1):
    w(f"## Path {k}: {p['path']}\n")
    if p.get("intro"): w(ref(p["intro"]) + "\n")
    for j, st in enumerate(p["steps"], 1):
        w(f"{j}. {album(st['id'])} — {ref(st.get('connection', ''))}")
    w("")

# 8
w('<div class="pagebreak"></div>\n\n# 8. Appendix: the borderline decisions\n')
app = essay("appendix") or {}
for p in app.get("paragraphs", []): w(ref(p) + "\n")
for d in app.get("decisions", []): w(f"- **{d['item']}.** {ref(d['text'])}")
w("")

os.makedirs(f"{OUT}/figs", exist_ok=True)
for f in ("v_lineage.png", "trunk_lines.png"):
    src = f"{W}/deliverables/figs/{f}"
    if os.path.abspath(src) != os.path.abspath(f"{OUT}/figs/{f}"): shutil.copy(src, f"{OUT}/figs/{f}")
open(f"{OUT}/V_Map.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
json.dump({"cited": sorted(cited), "missing": sorted(missing)}, open(f"{OUT}/md_cited_ids.json", "w"))
print(f"wrote {OUT}/V_Map.md: {len(out)} lines, {len(cited)} album IDs cited, missing: {sorted(missing) or 'none'}")
