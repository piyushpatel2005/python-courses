"""Original, deterministic diagrams 20..39. Run then build-second-half.mjs.
All examples are standalone teaching data, not exercise fixtures.
"""
from pathlib import Path
import json, html, bisect, heapq
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'assets/diagrams'
PLAN=json.loads((ROOT/'assets/diagram-plan.json').read_text())[20:40]
BLUE='#dbeafe'; GREEN='#dcfce7'; ORANGE='#ffedd5'; RED='#fee2e2'; PURPLE='#ede9fe'; INK='#183153'
checks=[]
def check(name,actual,expected):
    assert actual==expected,(name,actual,expected)
    checks.append(dict(name=name,actual=actual,expected=expected,passed=True))
from second_half_renderer import Drawing

# 20: binary search, each row shows the complete array and active interval.
a=[2,5,5,5,9,14];target=5;lo=0;hi=len(a);states=[]
while lo<hi:
    mid=(lo+hi)//2;states.append((lo,hi,mid))
    if a[mid]<target:lo=mid+1
    else:hi=mid
check('lower_bound(5)',lo,bisect.bisect_left(a,target))
d=Drawing('Lower bound keeps the first match','Sorted data • target 5 • candidate interval [lo, hi)',750)
for r,(l,h,m) in enumerate(states):
    y=110+r*160;d.text(300,y,f'lo={l}, hi={h}, mid={m} → value {a[m]}',22)
    d.array(a,y+18,colors={i:(ORANGE if i==m else GREEN) for i in range(l,h)},indices=True)
d.note(630,'Stop: lo = hi = 1. Insert before index 1.','Orange: midpoint. Green: other candidates.','Blue: outside the current candidate interval.');d.save(PLAN[0],ROOT,OUT)
# 21: stable merge.
left=[(3,'L'),(7,'L'),(10,'L')];right=[(4,'R'),(7,'R'),(12,'R')]
merged=sorted(left+right,key=lambda v:v[0]);check('stable merge',merged,[(3,'L'),(4,'R'),(7,'L'),(7,'R'),(10,'L'),(12,'R')])
d=Drawing('Merge: equal keys take left first','L / R tags show origin, not part of the sort key',690)
d.text(300,115,'Snapshot: 3L and 4R already emitted')
d.array(['3L','7L','10L'],145,x=35,w=175,colors={0:'#f1f5f9',1:ORANGE});d.text(300,225,'Left cursor: index 1 (7L)',21)
d.array(['4R','7R','12R'],260,x=35,w=175,colors={0:'#f1f5f9',1:ORANGE});d.text(300,340,'Right cursor: index 1 (7R)',21)
d.text(300,390,'Output prefix');d.array(['3L','4R','7L'],410,x=35,w=175,colors={2:GREEN})
d.note(500,'Tie 7 = 7: emit 7L, advance only left.','Then emit 7R, 10L; copy remaining tail 12R.')
d.array([str(v)+s for v,s in merged],580);d.save(PLAN[1],ROOT,OUT)
# 22: three-way partition.
a=[8,3,6,2,8,5,8];pivot=8;parts=[[v for v in a if v<pivot],[v for v in a if v==pivot],[v for v in a if v>pivot]]
check('partition multiset',sorted(sum(parts,[])),sorted(a))
d=Drawing('Three regions around pivot 8','Conceptual grouping • not an in-place swap trace',570)
d.text(300,115,'Input');d.array(a,135)
d.box(30,245,250,60,'less than 8',BLUE);d.box(300,245,150,60,'equal to 8',GREEN);d.box(470,245,100,60,'> 8',ORANGE)
d.array(parts[0],330,x=30,w=62);d.array(parts[1],330,x=300,w=50,colors={i:GREEN for i in range(3)});d.text(520,365,'empty',20)
d.note(450,'[3, 6, 2, 5] is NOT yet sorted.','Recursively sort the less / greater regions.');d.save(PLAN[2],ROOT,OUT)
# 23: traversals.
nodes={0:(300,150,11),1:(160,260,4),2:(440,260,18),3:(80,370,2),4:(240,370,7),5:(440,370,15)};edges=[(0,1),(0,2),(1,3),(1,4),(2,5)]
children={0:[1,2],1:[3,4],2:[5,None]}
def traverse(k,mode):
    if k is None:return []
    l,r=children.get(k,[None,None]);v=[nodes[k][2]];L=traverse(l,mode);R=traverse(r,mode)
    return v+L+R if mode=='pre' else L+v+R if mode=='in' else L+R+v
orders=[traverse(0,m) for m in ['pre','in','post']]
check('inorder BST',orders[1],[2,4,7,11,15,18]);check('postorder',orders[2],[2,7,4,15,18,11])
d=Drawing('Three walks, one binary tree','Left child is drawn to the left of its parent',670)
# Single left child must visibly be left of 18.
nodes[5]=(380,370,15);d.tree(nodes,edges)
for y,label,vals in zip([465,525,585],['Pre: root, left, right','In: left, root, right','Post: left, right, root'],orders):
    d.text(300,y,label,21);d.text(300,y+27,' → '.join(map(str,vals)),23)
d.save(PLAN[3],ROOT,OUT)
# 24 successor child transplant.
d=Drawing('Delete 20: transplant successor 26','Distinct keys • successor has a right child, 28',850)
before={0:(290,155,20),1:(100,250,9),2:(470,250,35),3:(360,345,26),4:(425,435,28)}
d.tree(before,[(0,1),(0,2),(2,3),(3,4)],{0:RED,3:GREEN,4:ORANGE})
d.text(92,155,'Before',22)
d.note(490,'26 is the minimum of the right subtree.','Detach 26: set 35.left to 28. Then replace 20.')
after={0:(290,605,26),1:(100,700,9),2:(470,700,35),3:(385,785,28)}
d.tree(after,[(0,1),(0,2),(2,3)],{0:GREEN,3:ORANGE});d.text(92,605,'After',22)
bst={20:[9,35],9:[None,None],35:[26,None],26:[None,28],28:[None,None]}
# Walk to the successor, detach its right child, transplant its node.
succ_parent=20;succ=bst[20][1]
while bst[succ][0] is not None:succ_parent,succ=succ,bst[succ][0]
bst[succ_parent][0]=bst[succ][1]
bst[succ]=bst[20];del bst[20]
def bst_inorder(k):
    return [] if k is None else bst_inorder(bst[k][0])+[k]+bst_inorder(bst[k][1])
check('successor transplant inorder',bst_inorder(succ),[9,26,28,35])
check('successor right child reattached',bst[35][0],28);d.save(PLAN[4],ROOT,OUT)
# 25 mapping.
heap=[3,8,6,14,11,10,9];check('min heap mapping',all(heap[(i-1)//2]<=heap[i] for i in range(1,len(heap))),True)
d=Drawing('One min-heap, two views','Each node shows index : value • zero-based indices',690)
n={0:(300,140,'0:3'),1:(160,245,'1:8'),2:(440,245,'2:6'),3:(70,350,'3:14'),4:(220,350,'4:11'),5:(380,350,'5:10'),6:(530,350,'6:9')};d.tree(n,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)],width=82)
d.array(heap,440,indices=True);d.note(565,'parent(i) = (i − 1) // 2, for i > 0','children: 2i + 1 and 2i + 2, if < n','Array indices encode links; no pointers stored.');d.save(PLAN[5],ROOT,OUT)
# 26 sift down.
orig=[2,5,4,9,7,8,6];h=orig.copy();popped=heapq.heappop(h);check('sift down after pop',h,[4,5,6,9,7,8])
d=Drawing('Sift down after removing minimum','Pop 2; move last value 6 to root; size becomes 6',930)
for y,vals,label,col in [(150,[6,5,4,9,7,8],'1. Compare 6 with children 5 and 4',{0:ORANGE,2:GREEN}),(440,[4,5,6,9,7,8],'2. Swap with smaller child 4',{0:GREEN,2:ORANGE})]:
    d.text(300,y-40,label,22)
    n={0:(300,y+5,vals[0]),1:(160,y+90,vals[1]),2:(440,y+90,vals[2]),3:(70,y+175,vals[3]),4:(240,y+175,vals[4]),5:(365,y+175,vals[5])}
    d.tree(n,[(0,1),(0,2),(1,3),(1,4),(2,5)],col)
d.note(720,'At index 2, only child is 8. Since 6 ≤ 8, stop.','Every parent is now ≤ its children.')
d.array(h,810,indices=True);d.save(PLAN[6],ROOT,OUT)
# 27 stable heap.
entries=[(2,0,'oak'),(1,1,'elm'),(2,2,'ash')];check('stable priority order',[e[2] for e in sorted(entries)],['elm','oak','ash'])
d=Drawing('Stable priority: counter breaks ties','Lower priority number wins • counter increases',620)
d.text(300,115,'Heap entries: (priority, counter, payload)',21)
n={0:(300,175,'1,1,elm'),1:(150,300,'2,0,oak'),2:(450,300,'2,2,ash')};d.tree(n,[(0,1),(0,2)],width=150)
d.text(300,385,'Pop order');d.array(['elm','oak','ash'],410,x=35,w=175)
d.note(510,'oak precedes ash: same priority, 0 < 2.','Unique counters prevent payload comparison.');d.save(PLAN[7],ROOT,OUT)
# 28 graph correspondence.
V=['P','Q','R','S'];E=[('P','Q'),('P','R'),('Q','S'),('R','S')];adj={v:sorted(b if a==v else a for a,b in E if v in (a,b)) for v in V};matrix=[[int(b in adj[a]) for b in V] for a in V];check('undirected matrix symmetry',matrix,[list(x) for x in zip(*matrix)])
d=Drawing('Same graph, three representations','Undirected • unweighted • no self-loops',820)
coords={'P':(170,145,'P'),'Q':(430,145,'Q'),'R':(170,300,'R'),'S':(430,300,'S')}
for a,b in E:
    x,y,_=coords[a];X,Y,_=coords[b];d.edge(x+(33 if X>x else 0),y+(25 if Y>y else 0),X-(33 if X>x else 0),Y-(25 if Y>y else 0))
for x,y,v in coords.values():d.node(x,y,v)
d.text(145,390,'Adjacency lists',22);d.text(420,390,'Matrix: P Q R S',22)
for i,v in enumerate(V):
    d.text(145,450+i*65,f'{v}: '+', '.join(adj[v]),23)
    d.text(300,450+i*65,v,22)
    for j,val in enumerate(matrix[i]):d.box(325+j*57,420+i*65,52,48,val,GREEN if val else '#f1f5f9',22)
d.note(740,'A 1 at row P, column Q matches edge P—Q.');d.save(PLAN[8],ROOT,OUT)
# 29 BFS.
d=Drawing('BFS discovers distance layers','Undirected cycle • scan neighbors alphabetically',760)
coords={'P':(100,260,'P'),'Q':(300,160,'Q'),'R':(300,360,'R'),'S':(500,260,'S')}
for a,b in E:
    x,y,_=coords[a];X,Y,_=coords[b];d.edge(x+33,y,X-33,Y)
for v,(x,y,t) in coords.items():d.node(x,y,t,GREEN if v=='P' else BLUE)
for x,txt in [(100,'distance 0'),(300,'distance 1'),(500,'distance 2')]:d.text(x,110,txt,20)
from collections import deque
q=deque(['P']);dist={'P':0};snap=[]
while q:
    u=q.popleft()
    for v in adj[u]:
        if v not in dist:dist[v]=dist[u]+1;q.append(v)
    snap.append((u,list(q)))
check('BFS distances',dist,{'P':0,'Q':1,'R':1,'S':2})
d.note(435,'Front of FIFO queue is at the left.')
for i,(u,queue) in enumerate(snap):d.text(300,485+45*i,f'After processing {u}:  ['+', '.join(queue)+']',23)
d.note(690,'Mark on enqueue: S is not queued twice.');d.save(PLAN[9],ROOT,OUT)
# 30 DFS cases.
d=Drawing('DFS: active is not finished','Directed edges • active = orange; finished = green',790)
d.text(300,115,'Case A: back edge proves a directed cycle',22)
d.node(100,190,'U',ORANGE);d.node(300,190,'V',ORANGE);d.node(500,190,'W',ORANGE)
d.edge(133,190,267,190,True);d.edge(333,190,467,190,True);d.edge(500,215,100,215,True,via=[(500,290),(100,290)])
d.note(335,'Active recursion path: U → V → W.','W → U reaches an active ancestor.')
d.text(300,440,'Case B: edge to a finished node is not enough',22)
d.node(100,520,'U',ORANGE);d.node(300,520,'V',ORANGE);d.node(500,520,'X',GREEN)
d.edge(133,520,267,520,True);d.edge(333,520,467,520,True);d.edge(100,495,500,495,True,via=[(100,465),(500,465)])
d.note(635,'U explored X first; X has already returned.','Now U explores V; V → X is not a back edge.','Case B is acyclic: U→V, U→X, V→X.');d.save(PLAN[10],ROOT,OUT)
# 31 relax.
check('relax via U',6+3,9)
d=Drawing('Relax an edge only when better','Directed weighted graph • strict improvement rule',610)
d.node(100,180,'S');d.node(300,180,'U');d.node(500,180,'V');d.edge(133,180,267,180,True);d.edge(333,180,467,180,True)
d.note(270,'Edge weights: S→U is 6; U→V is 3.','Known d[U] = 6; old d[V] = 13.')
d.box(60,365,210,70,'6 + 3 = 9',GREEN);d.box(330,365,210,70,'9 < 13',GREEN)
d.note(490,'Update d[V] = 9 and predecessor[V] = U.','If candidate ≥ old distance, keep both unchanged.');d.save(PLAN[11],ROOT,OUT)
# 32 stale.
check('Dijkstra improved record',3+2,5)
d=Drawing('Dijkstra skips an outdated record','Nonnegative weights • lazy duplicate heap entries',720)
d.node(100,160,'S');d.node(300,160,'U');d.node(500,160,'V');d.edge(133,160,267,160,True);d.edge(333,160,467,160,True);d.edge(100,185,500,185,True,via=[(100,270),(500,270)])
d.note(320,'Weights: S→U = 3; U→V = 2; S→V = 11.','Direct discovery queues (11,V). Via U finds 5.')
d.box(45,425,235,65,'(5, V): current',GREEN);d.box(320,425,235,65,'(11, V): stale',ORANGE)
d.note(545,'Distance table: d[V] = 5.','Pop (5,V): relax its outgoing edges.','Later pop (11,V): 11 ≠ d[V], so skip.','Heap records are not unique vertex objects.');d.save(PLAN[12],ROOT,OUT)
# 33 bits.
v=0b00101101;mask=255;check('masked complement',(~v)&mask,210)
d=Drawing('Keep a complement inside 8 bits','Bit 0 (least significant) is at the right',670)
d.text(300,115,'Bit positions');d.array(list(range(7,-1,-1)),135,colors={i:'#f1f5f9' for i in range(8)})
for y,label,num in [(235,'x = 45',v),(365,'mask = 255',mask),(495,'(~x) & mask = 210',(~v)&mask)]:
    d.text(300,y,label,23);d.array(f'{num:08b}',y+20,colors={i:GREEN for i,c in enumerate(f'{num:08b}') if c=='1'})
d.note(605,'Python ~45 = −46, not an unsigned 8-bit value.');d.save(PLAN[13],ROOT,OUT)
# 34 trie.
d=Drawing('Delete “map”, preserve “mat”','Node labels are edge characters • ★ marks a word',910)
for y,label,removed in [(150,'Before',False),(510,'After deleting map',True)]:
    d.text(110,y-30,label,22)
    n={0:(300,y,'root'),1:(300,y+85,'m'),2:(300,y+170,'a'),3:(190,y+255,'p ★'),4:(410,y+255,'t ★')}
    if removed:del n[3]
    d.tree(n,[(0,1),(1,2)]+([] if removed else [(2,3)])+[(2,4)],{3:RED,4:GREEN},width=85)
d.note(825,'Prune unused p only; m and a still lead to mat.');d.save(PLAN[14],ROOT,OUT)
# 35 Fenwick.
a=[4,1,7,2,6,3,5,8];bit=[0]+[sum(a[i-(i&-i):i]) for i in range(1,9)];i=7;path=[]
while i:path.append(i);i-=i&-i
check('Fenwick prefix(7)',sum(bit[i] for i in path),sum(a[:7]))
d=Drawing('Fenwick: prefix(7) uses three blocks','1-based indices • intervals below are inclusive',780)
d.array(a,110,indices=True,start=1)
for y,i in zip([245,345,445],path):
    low=i-(i&-i)+1;x=30+(low-1)*67.5;w=(i-low+1)*67.5-3
    d.box(x,y,w,52,bit[i],GREEN)
    d.text(300,y+85,f'tree[{i}] covers [{low}, {i}] → sum {bit[i]}',22)
d.note(610,'Query indices: 7 → 6 → 4 → 0.','Each step subtracts lowbit(i) = i & −i.','5 + 9 + 14 = 28 = sum of positions 1…7.');d.save(PLAN[15],ROOT,OUT)
# 36 segments.
a=[3,8,2,5];check('segment query [1,4)',sum(a[1:4]),15)
d=Drawing('Segment query uses disjoint cover','Zero-based • every interval is half-open [l, r)',710)
n={0:(300,150,'[0,4):18'),1:(150,270,'[0,2):11'),2:(450,270,'[2,4):7'),3:(75,395,'[0,1):3'),4:(225,395,'[1,2):8'),5:(375,395,'[2,3):2'),6:(525,395,'[3,4):5')}
d.tree(n,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)],{2:GREEN,4:GREEN},width=135)
d.text(300,475,'Original array');d.array(a,495,indices=True)
d.note(610,'Query [1,4) = [1,2) ∪ [2,4).','Green blocks: 8 + 7 = 15; no double counting.');d.save(PLAN[16],ROOT,OUT)
# 37 DSU.
parent={'A':'B','B':'C','C':'D','D':'D','X':'Y','Y':'Y'};old=parent.copy()
def find(x):
    if parent[x]!=x:parent[x]=find(parent[x])
    return parent[x]
check('DSU root',find('A'),'D');check('DSU compression',parent,{'A':'D','B':'D','C':'D','D':'D','X':'Y','Y':'Y'})
d=Drawing('Path compression changes parents','Arrows point to parents • root points to itself',860)
d.text(300,115,'Before find(A)')
for x,v in [(70,'A'),(220,'B'),(370,'C'),(520,'D')]:d.node(x,185,v,GREEN if v=='D' else BLUE)
for x,X in [(103,187),(253,337),(403,487)]:d.edge(x,185,X,185,True)
d.text(520,245,'root',20);d.node(220,320,'X');d.node(370,320,'Y',GREEN);d.edge(253,320,337,320,True);d.text(370,375,'root',20)
d.text(300,440,'After find(A): root is still D')
d.node(300,515,'D',GREEN)
for x,v in [(100,'A'),(300,'B'),(500,'C')]:d.node(x,645,v);d.edge(x,620,300,540,True)
d.node(220,750,'X');d.node(370,750,'Y',GREEN);d.edge(253,750,337,750,True)
d.text(300,810,'X→Y is unchanged; roots keep self-parents.',21);d.save(PLAN[17],ROOT,OUT)
# 38 backtrack.
from itertools import product
valid=[''.join(map(str,b)) for b in product([0,1],repeat=2) if sum(b)==1];check('backtracking exactly one 1',valid,['01','10'])
d=Drawing('Choose, recurse, undo','Length-2 bit strings with exactly one 1',760)
n={0:(300,150,'[]'),1:(150,270,'[0]'),2:(450,270,'[1]'),3:(75,410,'[0,0]'),4:(225,410,'[0,1]'),5:(375,410,'[1,0]'),6:(525,410,'[1,1]')}
d.tree(n,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)],{3:RED,4:GREEN,5:GREEN,6:RED},width=118)
for x,t in [(75,'reject'),(225,'emit'),(375,'emit'),(525,'prune')]:d.text(x,465,t,21)
d.note(535,'[1,1] has too many ones: prune immediately.','[0,0] reaches length 2 without one: reject.','At [0]: push 1 → recurse [0,1] → pop 1.','The undo restores [0] before returning to [].','Complete outputs: 01 and 10.');d.save(PLAN[18],ROOT,OUT)
# 39 responsibilities, actual miniature structures.
d=Drawing('Dispatch: separate responsibilities','Conceptual workbench • illustrative data only',930)
d.box(30,115,250,55,'Catalog lookup',PURPLE);d.box(320,115,250,55,'Pending FIFO',PURPLE)
d.box(30,185,250,55,'job7 → “north”',BLUE);d.array(['job7','job9'],185,x=320,w=125);d.text(445,275,'front at left',20)
d.box(30,320,250,55,'Priority heap',PURPLE);d.box(320,320,250,55,'History stack',PURPLE)
d.node(155,425,'1:job9',GREEN,w=130);d.node(155,515,'3:job7',BLUE,w=130);d.edge(155,450,155,490)
d.box(335,400,220,50,'assign job9 ← top',GREEN,20);d.box(335,460,220,50,'add job7',BLUE)
d.box(30,590,250,55,'Route graph',PURPLE);d.box(320,590,250,55,'Load sums',PURPLE)
d.node(85,705,'N');d.node(225,705,'E');d.edge(118,705,192,705)
d.array([4,6,3],675,x=320,w=83);d.text(445,780,'[0,2): 4 + 6 = 10',21)
d.note(850,'Queues choose next; graphs choose a route.','History supports undo; sums answer load queries.');d.save(PLAN[19],ROOT,OUT)
# Additional executable checks cover every displayed numeric/structural invariant.
check('lower-bound narrowing states',states,[(0,6,3),(0,3,1),(0,1,0)])
check('preorder',orders[0],[11,4,2,7,18,15])
check('Fenwick visited indices',path,[7,6,4])
check('Fenwick block values',[bit[i] for i in path],[5,9,14])
check('segment root sum',sum([3,8,2,5]),18)
check('segment half sums',[sum([3,8]),sum([2,5])],[11,7])
check('Python complement',~45,-46)
check('load query [0,2)',sum([4,6,3][0:2]),10)
def has_cycle(edges):
    graph={v:[] for edge in edges for v in edge}
    for u,v in edges:graph[u].append(v)
    colors={v:0 for v in graph}
    def visit(u):
        if colors[u]==1:return True
        if colors[u]==2:return False
        colors[u]=1
        if any(visit(v) for v in graph[u]):return True
        colors[u]=2;return False
    return any(visit(u) for u in graph if not colors[u])
check('DFS active ancestor cycle',has_cycle([('U','V'),('V','W'),('W','U')]),True)
check('DFS finished node DAG',has_cycle([('U','X'),('U','V'),('V','X')]),False)
trie={}
for word in ['map','mat']:
    node=trie
    for c in word:node=node.setdefault(c,{})
    node['$']=True
def delete_word(node,word,idx=0):
    if idx==len(word):del node['$']
    else:
        c=word[idx]
        if delete_word(node[c],word,idx+1):del node[c]
    return not node
delete_word(trie,'map')
check('trie prune preserves mat',trie,{'m':{'a':{'t':{'$':True}}}})
placements=[dict(index=i+20,**p,canonical_svg=str(OUT/p['file']),canonical_editable=str(OUT/p['editable']),local_svg=str(ROOT/p['lesson']/p['file']),local_editable=str(ROOT/p['lesson']/p['editable'])) for i,p in enumerate(PLAN)]
(OUT/'placements-second-half.json').write_text(json.dumps(placements,indent=2)+'\n')
(OUT/'checks-second-half.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({'diagrams':len(PLAN),'svg_files':len(PLAN)*2,'algorithm_checks':len(checks)}))
