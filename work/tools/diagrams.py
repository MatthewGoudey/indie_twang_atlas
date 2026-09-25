import json,re,subprocess,collections
W="/home/claude/work"; OUT=f"{W}/deliverables/figs"
lanes=json.load(open(f"{W}/skeleton/lanes.json")); L={l['id']:l for l in lanes}
def layer_of(l):
    if l['id']=='R1': return 'L6'
    m=re.search(r"(\d{4})",l['era']); y=int(m.group(1))
    if l['zone']=='Core': return 'L1'
    return "L1" if y>=2012 else "L2" if y>=1996 else "L3" if y>=1985 else "L4" if y>=1978 else "L5" if y>=1959 else "L6"
SHORT={"C1":"Indie twang","C2":"Barroom deadpan","C3":"New alt-country","C4":"Countrygaze","C5":"Twangy indie folk","C6":"Cosmic country","C7":"Slacker/jangle revival","C8":"Modern slowcore","C9":"Emo-twang",
"V1":"Molina circle","V2":"Drag City deadpan","V3":"Southern storytelling","V4":"Roots 2000s indie","V5":"Rootsy indie folk","V6":"2000s alt-country","V7":"New outlaw","V8":"American Primitive","V9":"No Depression","V10":"'90s slacker","V11":"Lo-fi","V12":"Slowcore","V13":"Americana songwriters","V14":"Cowpunk","V15":"Paisley Underground","V16":"College rock","V17":"Jangle/power pop","V18":"Flying Nun","V19":"'80s country rebels","V20":"Neil Young","V21":"Cosmic American","V22":"Dylan & The Band","V23":"Outlaw country","V24":"Texas songwriters","V25":"Country-folk storytellers","V26":"Honky-tonk/Bakersfield","V27":"Grateful Dead","V28":"Southern rock","V29":"Velvets/proto-indie","V30":"British folk rock","R1":"Roots",
"X1":"Nashville","X2":"Red Dirt/arena","X3":"Stomp-clap","X4":"Bluegrass","X5":"Chamber/freak folk","X6":"Emo","X7":"Heartland","X8":"Grunge","X9":"Shoegaze","X10":"Post-punk/noise","X11":"Modern Southern rock","X12":"Pop country turns","X13":"Laurel Canyon","X14":"Punk/hardcore"}
COL={"Core":"#F4A261","V":"#8FB8DE","Context":"#D0D0D0"}
LAYN={"L6":"L6 Roots (before 1965)","L5":"L5 Classic (1965–77)","L4":"L4 Underground (1978–86)","L3":"L3 Nineties (1987–97)","L2":"L2 Bridge (1998–2013)","L1":"L1 Now (2014–)"}
def wrap(s,n=22):
    out=[];cur=""
    for w in s.split():
        if len(cur)+len(w)>n: out.append(cur);cur=w
        else: cur=(cur+" "+w).strip()
    out.append(cur); return "\\n".join(out)
g=['digraph V {','graph [rankdir=TB, splines=true, nodesep=0.08, ranksep=0.55, bgcolor="white", fontname="Arial", label="The V — lineage of every lane (arrows: fed into). Orange = Core, blue = V, grey = Context", labelloc=t, fontsize=20];',
   'node [shape=box, style="rounded,filled", fontname="Arial", fontsize=13, penwidth=0.8, margin="0.06,0.03"];','edge [color="#55555588", arrowsize=0.6];']
by=collections.defaultdict(list)
for l in lanes: by[layer_of(l)].append(l)
order=["L6","L5","L4","L3","L2","L1"]
for l in list(by["L5"]):
    if l["zone"]=="Context": by["L5"].remove(l); by["L5x"].append(l)
for l in list(by["L3"]):
    if l["zone"]=="Context": by["L3"].remove(l); by["L3x"].append(l)
order=["L6","L5","L5x","L4","L3","L3x","L2","L1"]
LAYN["L5x"]="(Context, 1960s–70s)"; LAYN["L3x"]="(Context, '80s–'90s)"
for i,ly in enumerate(order):
    g.append(f'"{ly}" [shape=plaintext, style="", fontsize=13, label="{LAYN[ly]}"];')
for a,b in zip(order,order[1:]): g.append(f'"{a}" -> "{b}" [style=invis];')
for ly in order:
    # V lanes centre, context at edges
    ls=sorted(by[ly],key=lambda l:(0 if l['zone']!='Context' else 1, l['id']))
    ctx=[l for l in ls if l['zone']=='Context']; core=[l for l in ls if l['zone']!='Context']
    arranged=ctx[:len(ctx)//2]+core+ctx[len(ctx)//2:]
    ids=" ".join(f'"{l["id"]}"' for l in arranged)
    g.append(f'{{rank=same; "{ly}"; {ids}}}')
    for l in arranged:
        g.append(f'"{l["id"]}" [label="{l["id"]}\\n{wrap(SHORT[l["id"]],13)}", fillcolor="{COL[l["zone"]]}"];')
for l in lanes:
    for p in l['parents']:
        if p in L and p!=l['id']:
            st=' style=dashed' if L[p]['zone']=='Context' or l['zone']=='Context' else ''
            g.append(f'"{p}" -> "{l["id"]}" [{st}];')
g.append('}')
open(f"{OUT}/v_lineage.dot","w").write("\n".join(g))
subprocess.run(["dot","-Tpng","-Gdpi=170",f"{OUT}/v_lineage.dot","-o",f"{OUT}/v_lineage.png"],check=True)

# trunk lines
T=[("1 Crazy Horse guitar",["V20","V1","C1"],"Neil Young → Magnolia Electric Co. → MJ Lenderman"),
   ("2 Country by punk kids",["V14","V9","V6","C3"],"X, Jason & the Scorchers → Uncle Tupelo → Neko Case → Fust, Tobacco City"),
   ("3 Deadpan funny-sad",["V25","V2","C2"],"Prine, Tom T. Hall → Silver Jews → Ryan Davis & the Roadhouse Band"),
   ("4 Southern storytelling",["V28","V3","C4"],"Lynyrd Skynyrd → Drive-By Truckers → Wednesday"),
   ("5 Slow, sad, noisy",["V29","V12","C8"],"Velvet Underground → Low, Codeine → Friendship, Sluice"),
   ("6 The DIY network",["V16","V11","V10","C7"],"SST, R.E.M. → Guided by Voices → Pavement → Alex G, Horsegirl"),
   ("7 Cosmic American Music",["V21","V27","C6"],"Gram Parsons → Grateful Dead → Woods, Rose City Band"),
   ("8 Folk songwriting",["R1","V24","V5","C5"],"Carter Family, Guthrie → Townes → Gillian Welch → Big Thief")]
g=['digraph T {','graph [rankdir=TB, nodesep=0.25, ranksep=0.45, fontname="Arial", label="The eight trunk lines (top = oldest, bottom = today)", labelloc=t, fontsize=18];',
   'node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];','edge [color="#444444", penwidth=1.4, arrowsize=0.7];']
for i,(name,chain,ex) in enumerate(T):
    g.append(f'subgraph cluster_{i} {{ label="{wrap(name,18)}"; fontsize=12; fontname="Arial Bold"; color="#bbbbbb"; style=rounded;')
    for j,lid in enumerate(chain):
        g.append(f'"t{i}_{lid}" [label="{lid}\\n{wrap(L[lid]["name"],20)}", fillcolor="{COL[L[lid]["zone"]]}"];')
    g.append(f'"t{i}_ex" [shape=plaintext, style="", fontsize=9, label="{wrap(ex,24)}"];')
    for a,b in zip(chain,chain[1:]): g.append(f'"t{i}_{a}" -> "t{i}_{b}";')
    g.append(f'"t{i}_{chain[-1]}" -> "t{i}_ex" [style=invis];')
    g.append('}')
g.append('}')
open(f"{OUT}/trunk_lines.dot","w").write("\n".join(g))
subprocess.run(["dot","-Tpng","-Gdpi=170",f"{OUT}/trunk_lines.dot","-o",f"{OUT}/trunk_lines.png"],check=True)
print("ok")
