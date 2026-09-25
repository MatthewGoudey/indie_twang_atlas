#!/usr/bin/env python3
"""Apply description-review rewrites (qa/desc_result.jsonl, qa/descf_result_*.jsonl) to staging + master by (artist, album).
Skips already-applied ids (qa/desc_applied.jsonl). Validates length/sentences; logs flags to qa/desc_flags.jsonl."""
import json,glob,os,re,unicodedata,collections
W="/home/claude/work"; os.chdir(W)
def norm(s):
    s=unicodedata.normalize("NFKD",str(s)).encode("ascii","ignore").decode().lower().replace("&","and")
    s=re.sub(r"^the\s+","",s); return re.sub(r"[^a-z0-9]","",s)
master=[json.loads(l) for l in open("master.jsonl")]; byid={r['id']:r for r in master}
done=set()
if os.path.exists("qa/desc_applied.jsonl"): done={json.loads(l)['id'] for l in open("qa/desc_applied.jsonl")}
res={}
home={}
for f in glob.glob("qa/desc_batch_*.jsonl"):
    n=re.search(r"desc_batch_(\w+)\.jsonl",f).group(1)
    for l in open(f): home[json.loads(l)['id']]=f"qa/descf_result_{n}.jsonl"
for l in open("qa/desc_sample.jsonl"): home[json.loads(l)['id']]="qa/desc_result.jsonl"
def load(f):
    out={}
    if not os.path.exists(f): return out
    for l in open(f):
        try: q=json.loads(l)
        except: continue
        if isinstance(q,dict) and q.get('id') and q.get('verdict') in ('ok','rewrite','flag'): out.setdefault(q['id'],q)
    return out
files={f:load(f) for f in ["qa/desc_result.jsonl"]+sorted(glob.glob("qa/descf_result_*.jsonl"))}
missing=0
for i,hf in home.items():
    if i in done or i not in byid: continue
    q=files.get(hf,{}).get(i)
    if q is None:
        for f,d in files.items():
            if i in d: q=d[i]; break
    if q is None: missing+=1; continue
    res[i]=q
print("reviews missing:",missing)
def ok_desc(d):
    return d and len(d)>=110 and len(re.findall(r"[.!?](\s|$)",d))<=5 and not re.search(r'"[^"]{60,}"',d)
patch={}; flags=[]; cnt=collections.Counter(); bad=0
for i,q in res.items():
    cnt[q.get('verdict')]+=1
    if q.get('verdict')=='flag': flags.append({"id":i,"artist":byid[i]['artist'],"album":byid[i]['album'],"problems":q.get('problems')})
    rw=q.get('rewrite') or {}
    if q.get('verdict') in ('rewrite','flag') and rw:
        p={}
        if rw.get('description'):
            if ok_desc(rw['description']): p['description']=rw['description']
            else: bad+=1
        if rw.get('lineage') and len(rw['lineage'])>=40: p['lineage']=rw['lineage']
        if rw.get('lineage_basis') in ('Documented','Inferred','Both'): p['lineage_basis']=rw['lineage_basis']
        if p: patch[(norm(byid[i]['artist']),norm(byid[i]['album']))]=(i,p)
changed=set(); applied=set()
for f in sorted(glob.glob("staging/lane_*.jsonl")):
    lines=open(f,encoding="utf-8").readlines(); ch=False
    for n,l in enumerate(lines):
        if not l.strip(): continue
        r=json.loads(l)
        if r.get('needs_verification'): continue
        k=(norm(r['artist']),norm(r['album']))
        if k in patch:
            r.update(patch[k][1]); lines[n]=json.dumps(r,ensure_ascii=False)+"\n"; ch=True; applied.add(patch[k][0])
    if ch: open(f,"w",encoding="utf-8").writelines(lines); changed.add(f)
for k,(i,p) in patch.items(): byid[i].update(p)
with open("master.jsonl","w") as fo:
    for r in master: fo.write(json.dumps(r,ensure_ascii=False)+"\n")
with open("qa/desc_applied.jsonl","a") as fo:
    for i in res: fo.write(json.dumps({"id":i,"verdict":res[i].get('verdict')})+"\n")
with open("qa/desc_flags.jsonl","a") as fo:
    for x in flags: fo.write(json.dumps(x,ensure_ascii=False)+"\n")
print(dict(cnt),"patched",len(patch),"in staging",len(applied),"rejected desc",bad,"files",len(changed))
