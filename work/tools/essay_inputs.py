import json,collections,os
W="/home/claude/work"; os.chdir(W)
lanes={l['id']:l for l in json.load(open("skeleton/lanes.json"))}
rows=[json.loads(l) for l in open("master.jsonl")]
by=collections.defaultdict(list)
for r in rows: by[r['primary_lane']].append(r)
K=['id','artist','album','year','label','type','scene','base','priority','start_here','descriptors','description','lineage','lineage_basis','key_tracks','terry','secondary_lanes']
for lid,l in lanes.items():
    rs=sorted(by[lid],key=lambda r:(r['year'],r['artist']))
    json.dump({"lane":l,"albums":[{k:r.get(k) for k in K} for r in rs]},open(f"essays/input_{lid}.json","w"),ensure_ascii=False)
print("inputs",len(lanes))
