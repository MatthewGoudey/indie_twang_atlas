import json,glob,re
W="/home/claude/work"
master={}
for l in open(f"{W}/master.jsonl"):
    r=json.loads(l); master[r['id']]=r
out={}
def add(i,why):
    if i not in master: return
    out.setdefault(i,[]).append(why)
for f in glob.glob(f"{W}/qa/result_*.jsonl"):
    for l in open(f):
        try: q=json.loads(l)
        except: continue
        if q.get('verdict')=='fix' and not q.get('corrections'): add(q['id'],"QA: "+(q.get('note') or '')[:200])
        if q.get('verdict')=='unchecked': add(q['id'],"QA unchecked: "+(q.get('note') or '')[:150])
pat=re.compile(r"key[_ ]track|label|year|released in|came out in|not on (this|the) album|from (his|her|their) \d{4}|wrong artist|credited to",re.I)
for f in glob.glob(f"{W}/qa/desc*_result*.jsonl")+[f"{W}/qa/desc_result.jsonl"]:
    for l in open(f):
        try: q=json.loads(l)
        except: continue
        if q.get('verdict')=='flag': add(q['id'],"DESC flag: "+"; ".join(q.get('problems') or [])[:300])
        for p in q.get('problems') or []:
            if pat.search(p) and ('key_track' in p.lower() or 'key track' in p.lower() or 'label' in p.lower() or re.search(r"\b(19|20)\d\d\b",p)):
                if any(w in p.lower() for w in ['field','key_track','key track','label','year looks','probably','likely','not changed','outside']):
                    add(q['id'],"DESC note: "+p[:250])
rows=[]
for i,why in sorted(out.items()):
    r=master[i]; rows.append({"id":i,"artist":r['artist'],"album":r['album'],"year":r['year'],"type":r['type'],"label":r['label'],"key_tracks":r['key_tracks'],"sources":r['sources'],"issues":why})
with open(f"{W}/qa/residual_batch.jsonl","w") as fo:
    for r in rows: fo.write(json.dumps(r,ensure_ascii=False)+"\n")
print(len(rows))
