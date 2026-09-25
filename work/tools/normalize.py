#!/usr/bin/env python3
"""Post-merge normalization of master.jsonl: artist names, scenes, orchestrator overrides. Writes borderline_log.jsonl entries for overrides."""
import json,sys,os
sys.path.insert(0,'/home/claude/work/tools')
from scenes_def import canon
W="/home/claude/work"; os.chdir(W)
ov=json.load(open("overrides.json")); lanes={l['id']:l for l in json.load(open("skeleton/lanes.json"))}
rows=[json.loads(l) for l in open("master.jsonl")]
out=[]; log=[]; dropped=[]
def layer(y,lane):
    if lane=="R1": return "L6"
    return "L1" if y>=2014 else "L2" if y>=1998 else "L3" if y>=1987 else "L4" if y>=1978 else "L5" if y>=1965 else "L6"
for r in rows:
    r['artist']=ov['artist_names'].get(r['artist'],r['artist'])
    c=canon(r.get('scene',''))
    r['scene']=c if c else ""
    drop=False
    for o in ov['rows']:
        if o['artist']!=r['artist']: continue
        if o.get('album') and o['album']!=r['album']: continue
        if o.get('except_album') and o['except_album']==r['album']: continue
        if o.get('drop'): drop=True; dropped.append(r); break
        for k,v in o['set'].items(): r[k]=v
        r['secondary_lanes']=[s for s in r.get('secondary_lanes',[]) if s!=r['primary_lane']][:2]
        log.append({"item":f"{r['artist']} – {r['album']} ({r['year']})","id":r['id'],"decision":f"Primary lane set to {r['primary_lane']}","reason":o['reason']})
    if drop: continue
    sk=ov.get('start_here',{}).get(r['primary_lane'])
    if sk is not None: r['start_here']='Y' if r['album'] in sk else ''
    r['layer']=layer(r['year'],r['primary_lane']); r['zone']=lanes[r['primary_lane']]['zone']
    out.append(r)
for o in ov['rows']:
    if o.get('drop'): log.append({"item":f"{o['artist']}" + (f" – {o['album']}" if o.get('album') else " (all albums)"),"id":"","decision":"Excluded from Albums","reason":o['reason']})
for n in ov.get('notes',[]): log.append({"item":n['item'],"id":"","decision":n['decision'],"reason":n['reason']})
with open("master.jsonl","w") as f:
    for r in out: f.write(json.dumps(r,ensure_ascii=False)+"\n")
with open("borderline_log.jsonl","w") as f:
    for e in log: f.write(json.dumps(e,ensure_ascii=False)+"\n")
print("normalized",len(out),"dropped",len(dropped),"log",len(log))
