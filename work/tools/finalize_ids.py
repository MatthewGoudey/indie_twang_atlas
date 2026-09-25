#!/usr/bin/env python3
"""Final ID assignment (Phase 8): order by lane (C1..C9, V1..V30, R1, X1..X14), then year, artist, album.
Writes master.jsonl with new IDs and id_map.json {old: new}. Run ONLY after all QA results are applied."""
import json,os,re
W="/home/claude/work"; os.chdir(W)
lanes=[l['id'] for l in json.load(open("skeleton/lanes.json"))]
order={l:i for i,l in enumerate(lanes)}
rows=[json.loads(l) for l in open("master.jsonl")]
rows.sort(key=lambda r:(order[r['primary_lane']], r['year'], re.sub(r'^the ','',r['artist'].lower()), r['album'].lower()))
m={}
for i,r in enumerate(rows,1):
    new=f"A{i:04d}"; m[r['id']]=new; r['id']=new
with open("master.jsonl","w") as f:
    for r in rows: f.write(json.dumps(r,ensure_ascii=False)+"\n")
json.dump(m,open("id_map.json","w"),indent=0)
open("IDS_FINAL","w").write("IDs finalized; do not re-run merge.py without keeping master IDs.\n")
print("final ids", len(rows))
