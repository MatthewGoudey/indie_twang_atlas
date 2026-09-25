import json,glob,re,sys,unicodedata
sys.path.insert(0,'/home/claude/work/tools')
def norm(s):
    s=unicodedata.normalize("NFKD",str(s)).encode("ascii","ignore").decode().lower().replace("&","and")
    s=re.sub(r"^the\s+","",s); return re.sub(r"[^a-z0-9]","",s)
staged=set(); arts=set()
for f in glob.glob("/home/claude/work/staging/lane_*.jsonl"):
    for l in open(f):
        if not l.strip(): continue
        r=json.loads(l); staged.add((norm(r['artist']),norm(r['album']))); arts.add(norm(r['artist']))
for lane in sys.argv[1:]:
    out=[]
    for l in open(f"/home/claude/work/sources/terry_by_lane/{lane}.txt"):
        if l.startswith("#") or not l.strip(): continue
        p=[x.strip() for x in l.split("|")]
        a,al=p[0],p[1]
        k=(norm(a),norm(al))
        if k in staged: continue
        if any(k[0]==s[0] and (k[1] in s[1] or s[1] in k[1]) for s in staged if k[1] and s[1]): continue
        out.append(l.rstrip())
    open(f"/home/claude/work/sources/leftovers_{lane}.txt","w").write("\n".join(out)+"\n")
    print(lane,len(out))
