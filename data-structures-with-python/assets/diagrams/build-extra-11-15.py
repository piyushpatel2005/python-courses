"""Original worked examples; only additional-plan modules 11–15 are written."""
from pathlib import Path
import json, heapq, math
from collections import deque
from second_half_renderer import Drawing, BLUE,GREEN,ORANGE,RED,PURPLE,INK
ROOT=Path(__file__).resolve().parents[2]; OUT=Path(__file__).resolve().parent
PLAN=[p for p in json.loads((ROOT/'assets/additional-diagram-plan.json').read_text()) if 11<=int(p['lesson'][:2])<=15]
assert len(PLAN)==40
CHECKS=[]
def check(name,actual,expected):
    assert actual==expected,(name,actual,expected)
    CHECKS.append(json.loads(json.dumps({'check':name,'actual':actual,'expected':expected,'pass':True})))
def tree(d,vals,y=145,colors=None):
    pos=[(300,y),(165,y+100),(435,y+100),(90,y+200),(230,y+200),(370,y+200),(510,y+200)]
    nodes={i:(*pos[i],v) for i,v in enumerate(vals) if v is not None}
    d.tree(nodes,[( (i-1)//2,i) for i in nodes if i and (i-1)//2 in nodes],colors,True)
def graph(d,edges,y=155,vertices='ABCD',directed=False,colors=None):
    coords={'A':(100,y),'B':(310,y),'C':(100,y+145),'D':(310,y+145),'Z':(500,y+72)}
    for e in edges:
        a,b=e[:2];x,Y=coords[a];X,Y2=coords[b]
        dx,dy=X-x,Y2-Y;scale= max(abs(dx)/33,abs(dy)/25)
        d.edge(x+dx/scale,Y+dy/scale,X-dx/scale,Y2-dy/scale,directed)
        if len(e)>2:
            # Horizontal/vertical labels sit clear of their edge.
            d.text((x+X)/2+(25 if dx==0 else 0),(Y+Y2)/2-12,str(e[2]),21)
    for v in vertices:d.node(*coords[v],v,(colors or {}).get(v,BLUE))
def row(d,label,vals,y,colors=None):
    d.text(300,y,label,21);d.array(vals or ['empty'],y+18,colors=colors,indices=True)
def adj(d,m,y):
    for i,(k,v) in enumerate(m.items()):d.text(300,y+i*32,f'{k}: {v}',21)
def make(p):
    key=p['lesson'].split('/')[1][3:];module=int(p['lesson'][:2])
    titles={'reconstruct-weighted-path':'Recover the weighted path','unreachable-and-zero-weights':'Zero weight is still an edge','bottom-up-heapify':'Build a heap from the bottom','level-order-traversal':'Level order uses a queue','connected-components':'Restart for each component','add-undirected-edge':'Store both edge directions','preorder-traversal':'Preorder: node, left, right','inorder-traversal':'Inorder: left, node, right'}
    title=titles.get(key,key.replace('-',' ').capitalize())
    d=Drawing(title,'Worked trace • original illustrative values',900)
    if module==11:
        vals=[18,9,27,4,13,None,32]
        if key=='binary-node':
            tree(d,[18,9,27],145);d.note(405,'root.value = 18','root.left → 9     root.right → 27');tree(d,[9],550);d.note(645,'Leaf 9: left = None; right = None','Empty tree: root = None')
        elif key in ('count-nodes','tree-height'):
            tree(d,vals);iscount=key=='count-nodes';a=[6,3,2,1,1,None,1] if iscount else [3,2,2,1,1,None,1]
            tree(d,a,500, {0:GREEN});d.note(415,'Same links below; labels become '+('subtree counts' if iscount else 'heights in nodes'))
            d.note(795,'1 + left + right; None contributes 0' if iscount else '1 + max(left, right); None has height 0')
            check(key,a[0],6 if iscount else 3)
        elif key in ('preorder-traversal','inorder-traversal','level-order-traversal'):
            tree(d,vals)
            def visit(i,order):
                if i>=len(vals) or vals[i] is None:return []
                a=visit(2*i+1,order);b=visit(2*i+2,order)
                return [vals[i]]+a+b if order=='pre' else a+[vals[i]]+b
            seq=visit(0,'pre') if key.startswith('pre') else visit(0,'in') if key.startswith('inorder') else [v for v in vals if v is not None]
            row(d,'Visit sequence',seq,420,{i:GREEN for i in range(6)})
            if key.startswith('level'):
                row(d,'Queue after removing 18 (front at left)',[9,27],565);row(d,'After 9: both old and new levels coexist',[27,4,13],705)
            else:
                row(d,'Active recursive frames, root at left',[18,9,4],570)
                d.note(740,'Emit on entry' if key.startswith('pre') else 'Emit after the left subtree returns','An empty subtree emits nothing.')
            check(key,seq,{'preorder-traversal':[18,9,4,13,27,32],'inorder-traversal':[4,9,13,18,27,32],'level-order-traversal':[18,9,27,4,13,32]}[key])
        elif key in ('bst-search','bst-minimum'):
            colors={0:ORANGE,1:ORANGE,4:GREEN} if key=='bst-search' else {0:ORANGE,1:ORANGE,3:GREEN}
            tree(d,vals,colors=colors)
            if key=='bst-search':
                row(d,'Search 13: compare, choose one branch',[18,9,13],430)
                d.note(580,'13 < 18: left; 13 > 9: right; found','Missing 12: 18 → 9 → 13 → None','Only the searched path is followed.')
                check(key,[18,9,13],[18,9,13])
            else:
                row(d,'Follow left links; stop at the leftmost',[18,9,4],430)
                d.note(580,'4.left = None; return value 4','No links change; 13 is not examined.','An empty tree has no minimum.')
                check(key,min(v for v in vals if v is not None),4)
            d.note(770,'Cost depends on height, not just node count.')
        elif key in ('bst-insert','bst-delete-leaf','bst-delete-one-child'):
            before=[18,9,27,4,None,None,32] if key=='bst-insert' else vals
            after=before.copy()
            if key=='bst-insert':after[4]=13;msg=['Insert 13 along 18 → 9 → empty right','Set 9.right to the new node 13.','Empty root: insert 13 makes root = 13.'];hi=4
            elif key=='bst-delete-leaf':after[3]=None;msg=['Delete leaf 4: set 9.left = None.','No child subtree needs reconnecting.','Singleton deletion makes root = None.'];hi=1
            else:after[2]=32;after[6]=None;msg=['Delete 27: replace its parent link by 32.','Set 18.right to the existing child 32.','Deleting a one-child root promotes its child.'];hi=2
            tree(d,before);d.note(415,'Before ↑     After ↓');tree(d,after,500,{hi:GREEN});d.note(760,*msg)
            check(key,sorted(v for v in after if v is not None), sorted(([v for v in before if v is not None]+[13]) if key=='bst-insert' else [v for v in before if v is not None and v!=(4 if key=='bst-delete-leaf' else 27)]))
        else:
            tree(d,[18,9,27,4,21],colors={4:RED});d.note(415,'21 > 9 passes its direct-parent comparison.','But 21 belongs to the LEFT subtree of 18.');row(d,'Bounds inherited down 18 → 9 → 21',['< 18','9 < x','x < 18'],540);d.note(720,'Required interval at 21: 9 < x < 18','21 violates the upper bound: invalid BST.','Strict bounds reject duplicate keys too.')
            check(key,9<21<18,False)
    elif module==12:
        if key=='heap-order':
            a=[3,8,6,15,11,10];tree(d,a);row(d,'Array slots are level order, not sorted',a,420);d.note(600,'Each parent ≤ each child; 8 > 6 is allowed.','For i = 1: children at 3 and 4 hold 15, 11.','A missing right child is not a violation.');check(key,all(a[(i-1)//2]<=a[i] for i in range(1,len(a))),True)
        elif key=='sift-up':
            a=[3,8,6,15,1,10];tree(d,a,colors={4:ORANGE});row(d,'Decrease index 4 to 1; compare with parent 8',a,420)
            a[4],a[1]=a[1],a[4];row(d,'Swap 4↔1; compare 1 with root 3',a,550,{1:ORANGE})
            a[1],a[0]=a[0],a[1];row(d,'Swap 1↔0; stop at root',a,680,{0:GREEN})
            d.note(820,'Parent index = (i - 1) // 2; repair one path.')
            check(key,a,[1,3,6,15,8,10])
        elif key=='heap-push':
            a=[3,8,6,15,11,10];before=a+[2];heapq.heappush(a,2);tree(d,before,colors={6:ORANGE});row(d,'Append 2 at index 6',before,420);row(d,'Swap 6↔2, then 2↔0',a,560,{0:GREEN});d.note(740,'Parent index is (i - 1) // 2.','Stop at root or when parent ≤ child.','Push into [] gives [2]; no swaps.');check(key,a,[2,8,3,15,11,10,6])
        elif key=='heap-pop':
            a=[3,8,6,15,11,10];out=heapq.heappop(a);tree(d,[10,8,6,15,11],colors={0:ORANGE});d.note(415,'Return 3; move last value 10 to root.');row(d,'Swap with smaller child 6',a,490,{0:GREEN});d.note(680,'Stop: both remaining subtrees satisfy order.','Singleton [3] → []; return 3.','Empty pop has no value (IndexError).');check(key,[out,a],[3,[6,8,10,15,11]])
        elif key=='bottom-up-heapify':
            a=[12,7,9,2,5,4];tree(d,a)
            a[2],a[5]=a[5],a[2];row(d,'i = 2: swap 9 with its only child 4',a,420,{2:GREEN})
            a[1],a[3]=a[3],a[1];row(d,'i = 1: swap 7 with smaller child 2',a,550,{1:GREEN})
            heapq.heapify(a);row(d,'i = 0: 12 moves down through 2, then 5',a,680,{0:GREEN})
            d.note(820,'Leaves need no repair; bottom-up build is O(n).');check(key,a,[2,5,4,7,12,9])
        elif key=='max-heap':
            a=[16,12,14,5,7,9];tree(d,a);row(d,'Max-heap array: parent ≥ children',a,420);row(d,'Remove 16; move 9 up; swap with 14',[14,12,9,5,7],570);d.note(750,'Choose the LARGER child while sifting down.','A max-heap is still not a sorted array.');check(key,all(a[(i-1)//2]>=a[i] for i in range(1,len(a))),True)
        elif key=='heap-sort':
            tree(d,[16,12,14,5,7,9]);row(d,'Swap root with last; exclude last slot',[9,12,14,5,7,16],420,{5:GREEN});row(d,'Repair only the active prefix',[14,12,9,5,7,16],560,{5:GREEN});row(d,'Repeat: ascending sorted result',[5,7,9,12,14,16],700,{i:GREEN for i in range(6)});check(key,sorted([16,12,14,5,7,9]),[5,7,9,12,14,16])
        elif key=='priority-updates':
            tree(d,['2:B','7:A','5:C']);row(d,'New priority A=1; old (7,A) stays stale',['1:A','2:B','5:C','7:A'],420,{0:GREEN,3:RED});d.note(590,'Current priorities: A=1, B=2, C=5','Pop 1:A, then 2:B, then 5:C.','When 7:A reaches root, discard it.');row(d,'Valid removal order',['A','B','C'],710);check(key,[x[1] for x in sorted([(1,'A'),(2,'B'),(5,'C')])],['A','B','C'])
        else:
            a=[7,12,9];heapq.heapify(a);tree(d,a);row(d,'k=3: retain largest values; minimum is 7',a,420);heapq.heappushpop(a,5);row(d,'Incoming 5 rejected: heap unchanged',a,550);heapq.heappushpop(a,14);row(d,'Incoming 14 replaces minimum 7',a,680,{0:GREEN});d.note(820,'Before k values arrive, push without evicting.');check(key,sorted(a),[9,12,14])
    elif module==13:
        if key=='adjacency-list':
            graph(d,[],vertices='ABC');adj(d,{'A':[],'B':[],'C':[]},400);d.note(580,'Input labels: A, B, A, C','One key per distinct vertex; no edges yet.','Three independent empty neighbor lists.','Isolated C is present; missing Z is absent.');check(key,list(dict.fromkeys('ABAC')),['A','B','C'])
        elif key=='add-vertex':
            graph(d,[('A','B')],vertices='AB');d.note(380,'Before: A:[B], B:[A]');graph(d,[('A','B')],510,vertices='ABC',colors={'C':GREEN});d.note(735,'Add C → True; C gets a fresh empty list.','Add A again → False; preserve A:[B].');check(key,len(dict(A=['B'],B=['A'],C=[])),3)
        elif key=='add-undirected-edge':
            graph(d,[],vertices='ABC');d.note(380,'Before: A:[], B:[], C:[]');graph(d,[('A','B')],510,vertices='ABC');d.note(735,'Add A—B → True: A:[B], B:[A], C:[]','Repeat B—A → False; no parallel edge.','Missing endpoint / self-loop: reject first.');check(key,{'A':['B'],'B':['A'],'C':[]}, {'A':['B'],'B':['A'],'C':[]})
        elif key=='remove-edge':
            graph(d,[('A','B'),('A','C')],vertices='ABC');d.note(380,'Remove A—B, but keep both vertex keys.');graph(d,[('A','C')],510,vertices='ABC',colors={'B':ORANGE});d.note(735,'After: A:[C], B:[], C:[A]','Repeat removal → False; state unchanged.');check(key,[e for e in [('A','B'),('A','C')] if e!=('A','B')],[('A','C')])
        elif key=='remove-vertex':
            graph(d,[('A','B'),('A','C'),('B','D')]);d.note(380,'Remove A: snapshot its neighbors [B, C].');graph(d,[('B','D')],510,vertices='BCD');d.note(735,'Remove A from B and C; then delete key A.','After: B:[D], C:[], D:[B]','Do not iterate the live shrinking list.');check(key,'A' in {'B':['D'],'C':[],'D':['B']},False)
        else:
            graph(d,[('A','B'),('B','D')],directed=True);adj(d,{'A':['B'],'B':['D'],'C':[],'D':[]},405);d.note(590,'Only outgoing neighbors are stored.','A → B does not imply B → A.');d.text(300,680,'Adjacency matrix (rows → columns A B D)',21)
            for i,(label,values) in enumerate([('A',[0,1,0]),('B',[0,0,1]),('D',[0,0,0])]):
                d.text(90,730+i*48,label,20)
                for j,v in enumerate(values):d.box(165+j*95,700+i*48,80,42,str(v),GREEN if v else BLUE,20)
            check(key,[[0,1,0],[0,0,1],[0,0,0]],[[0,1,0],[0,0,1],[0,0,0]])
    elif module==14:
        edges=[('A','B'),('A','C'),('B','D'),('C','D')]
        if key=='connected-components':
            graph(d,[('A','B'),('C','D')],vertices='ABCDZ',colors={'C':GREEN,'D':GREEN,'Z':ORANGE});row(d,'Outer scan restarts at unvisited C, then Z',['A B','C D','Z'],440);d.note(620,'Three components; Z counts despite no edges.','Reuse one visited set across all starts.','Empty graph has zero components.');check(key,3,3)
        elif key=='undirected-cycle':
            graph(d,edges,colors={'A':ORANGE,'C':RED});row(d,'DFS active path (root at left)',['A','B','D','C'],440);d.note(620,'At C: D is its parent, so ignore C—D.','A is visited and is NOT the parent of C.','C—A closes cycle A—B—D—C—A.','A single edge to a parent is not a cycle.');check(key,len(edges),4)
        elif key=='topological-order':
            graph(d,edges,directed=True);row(d,'Initial indegrees (A, B, C, D)',[0,1,1,2],420);row(d,'After removing A: ready queue (front left)',['B','C'],550);row(d,'Remove B then C; D becomes ready',['A','B','C','D'],680);d.note(820,'If output has fewer than V nodes: a cycle.');check(key,all('ABCD'.index(a)<'ABCD'.index(b) for a,b in edges),True)
        else:
            graph(d,edges,vertices='ABCDZ')
            if key=='bfs-frontier':
                row(d,'After A: queue front → back',['B','C'],420);row(d,'After B: C was already waiting',['C','D'],550);d.note(725,'Mark D on enqueue; C must not enqueue D again.','The frontier spans adjacent distance layers.','Queue memory follows breadth, not depth.');check(key,['C','D'],['C','D'])
            elif key=='bfs-traversal':
                row(d,'Visit order from A; B before C',['A','B','C','D'],420);row(d,'Queue after each visit',['B C','C D','D','empty'],550);d.note(725,'Visited on discovery: A, B, C, D','Z is unreachable from A and never enqueued.');check(key,list('ABCD'),list('ABCD'))
            elif key=='bfs-path':
                row(d,'Predecessors of (A, B, C, D)',['None','A','A','B'],420);row(d,'Follow D → B → A, then reverse',['A','B','D'],550);d.note(725,'Shortest path has 2 edges; A—C—D ties.','First discovery with B first chooses B.','A to A: [A]; A to Z: no path.');check(key,len(['A','B','D'])-1,2)
            elif key=='dfs-recursive':
                row(d,'Active calls at deepest point',['A','B','D','C'],420);row(d,'Discovery order (neighbors alphabetical)',['A','B','D','C'],550);d.note(725,'C sees only visited neighbors; return to D.','Then return to B and A; skip visited C.','Mark before recursing to avoid cycling.');check(key,list('ABDC'),list('ABDC'))
            else:
                row(d,'Stack bottom → top; pop from right',['C','B'],420);row(d,'Pop B; push D (mark on push)',['C','D'],550);d.note(725,'Pop D: C already discovered; do not push again.','Visit order: A, B, D, C; parent(C) stays A.','Same visit order need not mean same DFS tree.');check(key,['A','B','D','C'],list('ABDC'))
    else:
        edges=[('A','B',6),('A','C',2),('C','D',3),('B','D',1)]
        graph(d,edges,vertices='ABCDZ',directed=True)
        if key=='weighted-adjacency':
            adj(d,{'A':[('B',6),('C',2)],'B':[('D',1)],'C':[('D',3)],'D':[],'Z':[]},405);d.note(650,'Each outgoing entry stores neighbor AND weight.','D has incoming edges, but no outgoing edges.','Z is isolated. No missing reverse arcs are added.');check(key,sum(len(v) for v in {'A':[1,2],'B':[1],'C':[1],'D':[],'Z':[]}.values()),4)
        elif key=='path-cost':
            row(d,'A → B → D: cumulative costs',[0,6,7],430);row(d,'A → C → D: cumulative costs',[0,2,5],570,{2:GREEN});d.note(750,'Both paths use 2 edges; weights break the tie.','Cost sums edges, not visited vertices.','A one-vertex path has cost 0.');check(key,[6+1,2+3],[7,5])
        elif key=='dijkstra-scan':
            row(d,'Distances after settling A (A B C D Z)',[0,6,2,'∞','∞'],420);row(d,'Scan chooses C=2; relax C→D (2+3)',[0,6,2,5,'∞'],550,{3:GREEN});row(d,'Settle D=5 before B=6; stop at ∞',['A','C','D','B'],680);d.note(820,'Require nonnegative weights; scan costs O(V²+E).');check(key,[0,6,2,5],[0,6,2,2+3])
        elif key=='reconstruct-weighted-path':
            row(d,'Predecessor table (A B C D Z)',['None','A','A','C','None'],420);row(d,'Walk backward from D',['D','C','A'],550);row(d,'Reverse once: returned path',['A','C','D'],680,{i:GREEN for i in range(3)});d.note(820,'Check reachability before following predecessors.');check(key,list(reversed(['D','C','A'])),['A','C','D'])
        else:
            # Replace the first graph rather than cover it with another drawing.
            d=Drawing(title,'Worked trace • original illustrative values',900)
            graph(d,[('A','B',0),('A','C',4),('B','D',0)],vertices='ABCDZ',directed=True)
            row(d,'Final distance from A (A B C D Z)',[0,0,4,0,'∞'],420,{1:GREEN,3:GREEN,4:ORANGE});row(d,'Zero-cost path still contains real edges',['A','B','D'],570);d.note(750,'A→B has weight 0; absent A→Z is not 0.','Z stays ∞ with no predecessor; no path.','Relax only strict improvements to avoid repeats.');check(key,0+0,0)
    return d
# Independently execute the pointer/frontier algorithms behind the captions.
def algorithm_acceptance():
    class Node:
        def __init__(self,v):self.v=v;self.left=None;self.right=None
    def insert(t,v):
        if t is None:return Node(v)
        if v<t.v:t.left=insert(t.left,v)
        elif v>t.v:t.right=insert(t.right,v)
        return t
    def inorder(t):return inorder(t.left)+[t.v]+inorder(t.right) if t else []
    def count(t):return 1+count(t.left)+count(t.right) if t else 0
    def height(t):return 1+max(height(t.left),height(t.right)) if t else 0
    def delete(t,v):
        if t is None:return None
        if v<t.v:t.left=delete(t.left,v)
        elif v>t.v:t.right=delete(t.right,v)
        elif not t.left:return t.right
        elif not t.right:return t.left
        else:
            s=t.right
            while s.left:s=s.left
            t.v=s.v;t.right=delete(t.right,s.v)
        return t
    def fresh():
        t=None
        for v in [18,9,27,4,13,32]:t=insert(t,v)
        return t
    t=fresh();check('computed binary links',[t.v,t.left.v,t.right.v,t.left.left.left],[18,9,27,None])
    check('computed count/height/base cases',[count(t),height(t),count(None),height(None),height(Node(9))],[6,3,0,0,1])
    for target,expected in [(13,[18,9,13]),(12,[18,9,13])]:
        cur=t;trace=[]
        while cur:
            trace.append(cur.v)
            if cur.v==target:break
            cur=cur.left if target<cur.v else cur.right
        check('computed search '+str(target),trace,expected)
        check('computed found '+str(target),cur is not None,target==13)
    cur=t;trace=[]
    while cur:trace.append(cur.v);cur=cur.left
    check('computed minimum path',trace,[18,9,4])
    check('computed duplicate insertion',count(insert(t,13)),6)
    check('computed leaf deletion',inorder(delete(fresh(),4)),[9,13,18,27,32])
    check('computed one-child deletion',inorder(delete(fresh(),27)),[4,9,13,18,32])
    check('computed singleton deletion',delete(Node(4),4),None)
    q=deque([t]);order=[];frontiers=[]
    while q:
        n=q.popleft();order.append(n.v)
        q.extend(c for c in [n.left,n.right] if c);frontiers.append([c.v for c in q])
    check('computed tree BFS',order,[18,9,27,4,13,32]);check('computed tree frontier',frontiers[:2],[[9,27],[27,4,13]])
    g={v:[] for v in 'ABCDZ'}
    for a,b in [('A','B'),('A','C'),('B','D'),('C','D')]:g[a].append(b);g[b].append(a)
    q=deque('A');pred={'A':None};order=[];frontiers=[]
    while q:
        u=q.popleft();order.append(u)
        for v in g[u]:
            if v not in pred:pred[v]=u;q.append(v)
        frontiers.append(list(q))
    check('computed graph BFS',order,list('ABCD'));check('computed graph queue',frontiers,[list('BC'),list('CD'),['D'],[]]);check('computed BFS predecessor',pred,{'A':None,'B':'A','C':'A','D':'B'})
    def recover(pred,target):
        if target not in pred:return []
        result=[]
        while target is not None:result.append(target);target=pred[target]
        return result[::-1]
    check('computed BFS path',recover(pred,'D'),list('ABD'));check('computed BFS unreachable',recover(pred,'Z'),[])
    visited=set();order=[];parents={}
    def dfs(u,parent=None):
        visited.add(u);order.append(u);parents[u]=parent
        for v in g[u]:
            if v not in visited:dfs(v,u)
    dfs('A');check('computed recursive DFS',order,list('ABDC'));check('computed recursive parent C',parents['C'],'D')
    stack=['A'];visited={'A'};order=[];parents={}
    while stack:
        u=stack.pop();order.append(u)
        for v in reversed(g[u]):
            if v not in visited:visited.add(v);parents[v]=u;stack.append(v)
    check('computed iterative DFS',order,list('ABDC'));check('computed iterative parent C',parents['C'],'A')
    def cycle(u,parent,seen):
        seen.add(u)
        for v in g[u]:
            if v==parent:continue
            if v in seen or cycle(v,u,seen):return True
        return False
    check('computed undirected cycle',cycle('A',None,set()),True)
    g={'A':['B'],'B':['A'],'C':['D'],'D':['C'],'Z':[]};visited=set();components=[]
    for u in g:
        if u not in visited:
            order=[];dfs(u);components.append(order)
    check('computed components',components,[list('AB'),list('CD'),['Z']])
    g={'A':['B','C'],'B':['D'],'C':['D'],'D':[]};degree={u:0 for u in g}
    for neighbors in g.values():
        for v in neighbors:degree[v]+=1
    check('computed initial indegrees',list(degree.values()),[0,1,1,2])
    q=deque(u for u in g if degree[u]==0);order=[]
    while q:
        u=q.popleft();order.append(u)
        for v in g[u]:
            degree[v]-=1
            if degree[v]==0:q.append(v)
    check('computed Kahn order',order,list('ABCD'))
    check('computed directed matrix',[[int(v in g[u]) for v in 'ABD'] for u in 'ABD'],[[0,1,0],[0,0,1],[0,0,0]])
    def dijkstra(edges):
        g={u:[] for u in 'ABCDZ'}
        for u,v,w in edges:g[u].append((v,w))
        dist={u:math.inf for u in g};dist['A']=0;pred={'A':None};done=set();order=[];states=[]
        while len(done)<len(g):
            u=min((u for u in g if u not in done),key=dist.get)
            if dist[u]==math.inf:break
            done.add(u);order.append(u)
            for v,w in g[u]:
                if dist[u]+w<dist[v]:dist[v]=dist[u]+w;pred[v]=u
            states.append([str(dist[v]) if math.isinf(dist[v]) else dist[v] for v in g])
        return dist,pred,order,states
    dist,pred,order,states=dijkstra([('A','B',6),('A','C',2),('C','D',3),('B','D',1)])
    check('computed Dijkstra settled order',order,list('ACDB'));check('computed relaxation states',states[:2],[[0,6,2,'inf','inf'],[0,6,2,5,'inf']]);check('computed weighted path',recover(pred,'D'),list('ACD'))
    dist,pred,_,_=dijkstra([('A','B',0),('A','C',4),('B','D',0)])
    check('computed zero edges',[dist[v] for v in 'ABCD'],[0,0,4,0]);check('computed unreachable',math.isinf(dist['Z']),True)
    # Mutation contracts: independent lists, symmetric edges, and retained isolates.
    g={v:[] for v in 'ABC'};check('computed independent lists',len({id(v) for v in g.values()}),3)
    g['A'].append('B');g['B'].append('A');check('computed add edge',g,{'A':['B'],'B':['A'],'C':[]})
    g['A'].remove('B');g['B'].remove('A');check('computed remove edge',g,{'A':[],'B':[],'C':[]})
    g={'A':['B','C'],'B':['A','D'],'C':['A'],'D':['B']}
    for v in list(g['A']):g[v].remove('A');g['A'].remove(v)
    del g['A'];check('computed remove vertex',g,{'B':['D'],'C':[],'D':['B']})
    h=[(2,'B'),(7,'A'),(5,'C')];heapq.heappush(h,(1,'A'));check('computed lazy physical heap',h,[(1,'A'),(2,'B'),(5,'C'),(7,'A')]);current={'A':1,'B':2,'C':5};order=[];stale=[]
    while h:
        priority,task=heapq.heappop(h)
        if current.get(task)!=priority:stale.append(task);continue
        order.append(task);del current[task]
    check('computed lazy valid pops',order,list('ABC'));check('computed stale skip',stale,['A'])
    h=[-x for x in [16,12,14,5,7,9]];heapq.heappop(h);check('computed max pop',[-x for x in h],[14,12,9,5,7])
    h=[-x for x in [16,12,14,5,7,9]];result=[]
    while h:result.insert(0,-heapq.heappop(h))
    check('computed heap extraction sort',result,[5,7,9,12,14,16])
algorithm_acceptance()
for p in PLAN:
    make(p).save(p,ROOT,OUT)
placements=[{**p,'alt':p['file'].removesuffix('.svg').replace('-',' ')} for p in PLAN]
(OUT/'placements-extra-11-15.json').write_text(json.dumps(placements,indent=2)+'\n')
(OUT/'checks-extra-11-15.json').write_text(json.dumps(CHECKS,indent=2)+'\n')
print(json.dumps({'diagrams':len(PLAN),'checks':len(CHECKS)}))
