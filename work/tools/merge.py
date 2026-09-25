#!/usr/bin/env python3
"""Merge staging/lane_*.jsonl -> master.jsonl (keeps existing IDs), needs_verification.jsonl."""
import json,glob,re,os,datetime,collections,unicodedata
W="/home/claude/work"; os.chdir(W)
lanes={l['id']:l for l in json.load(open("skeleton/lanes.json"))}
def norm(s):
    s=unicodedata.normalize("NFKD",str(s)).encode("ascii","ignore").decode().lower()
    s=s.replace("&","and"); s=re.sub(r"^the\s+","",s)
    return re.sub(r"[^a-z0-9]","",s)
def key(r): return (norm(r['artist']),norm(r['album']))
def layer(y,lane):
    if lane=="R1": return "L6"
    return "L1" if y>=2014 else "L2" if y>=1998 else "L3" if y>=1987 else "L4" if y>=1978 else "L5" if y>=1965 else "L6"
old={}
if os.path.exists("master.jsonl"):
    for l in open("master.jsonl"):
        r=json.loads(l); old[key(r)]=r['id']
files=sorted(glob.glob("staging/lane_*.jsonl"), key=lambda f:(os.path.getmtime(f) if False else 0, f))
# stable order: previous-session files first (alphabetical), then new files alphabetical
rows=[];nv=[];dups=[];seen={}
for f in files:
    for i,l in enumerate(open(f,encoding="utf-8")):
        l=l.strip()
        if not l: continue
        try: r=json.loads(l)
        except Exception: print("BAD JSON",f,i+1); continue
        r['_file']=f
        if r.get("needs_verification"): nv.append(r); continue
        k=key(r)
        if k in seen: dups.append(f"{r['artist']} – {r['album']} ({f} dup of {seen[k]})"); continue
        seen[k]=f; rows.append(r)
nextid=max([int(v[1:]) for v in old.values()]+[0])+1
out=[]
for r in rows:
    k=key(r)
    if k in old: r['id']=old[k]
    else: r['id']=f"A{nextid:04d}"; nextid+=1
    r['layer']=layer(r['year'],r['primary_lane']); r['zone']=lanes[r['primary_lane']]['zone']
    out.append(r)
out.sort(key=lambda r:r['id'])
vk={key(r) for r in out}; nvk=set(); nv2=[]
for r in nv:
    k=key(r)
    if k in vk or k in nvk: continue
    nvk.add(k); nv2.append(r)
with open("master.jsonl","w") as f:
    for r in out: f.write(json.dumps(r,ensure_ascii=False)+"\n")
with open("needs_verification.jsonl","w") as f:
    for r in nv2: f.write(json.dumps(r,ensure_ascii=False)+"\n")
ts=datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
os.system(f"cp master.jsonl checkpoints/master_{ts}.jsonl")
lz=collections.Counter((r['layer'],r['zone']) for r in out)
ln=collections.Counter(r['primary_lane'] for r in out)
msg=f"# Merge {ts}\nrows {len(out)}, nv {len(nv2)}, dups dropped {len(dups)}\nlayer x zone: {dict(sorted(lz.items()))}\nby lane: {dict(sorted(ln.items()))}\ndups: {dups}\n"
open(f"logs/merge_{ts}.md","w").write(msg); print(msg)
