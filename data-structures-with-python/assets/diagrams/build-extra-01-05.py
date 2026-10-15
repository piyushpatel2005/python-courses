"""Original operation diagrams. Run with Python 3; companion acceptance uses build-extra-01-05.mjs.
Only writes the 32 planned extra figures in modules 01–05, their copies, placements and own audit.
All figures use independent explicitly labeled illustrative data, not assessed examples.
"""
from __future__ import annotations
import hashlib
import html
import json
from pathlib import Path
import math
from collections.abc import Sequence

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'assets/diagrams'
SCRATCH = Path.home() / '.hermes/profiles/curriculum-dev/cache/scratch/ds-diagrams-extra-01-05'
BLUE, GREEN, ORANGE, PURPLE, RED = '#dbeafe', '#dcfce7', '#ffedd5', '#ede9fe', '#fee2e2'
INK = '#172554'
plan = [p for p in json.loads((ROOT/'assets/additional-diagram-plan.json').read_text()) if int(p['lesson'][:2]) <= 5]
assert len(plan) == 32
checks: dict[str, object] = {}

class Drawing:
    def __init__(self, title: str, subtitle: str):
        self.parts = []
        self.text(620, 43, title, 28)
        self.text(620, 79, 'Original illustrative data • ' + subtitle, 18)
    def text(self, x: float, y: float, text: object, size: int=20, color: str=INK):
        self.parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial, sans-serif" font-size="{size}" fill="{color}">{html.escape(str(text))}</text>')
    def box(self, x: float, y: float, w: float, h: float, lines: list[str], fill: str=BLUE):
        self.parts.append(f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{INK}" stroke-width="1.5"/>')
        for i, line in enumerate(lines):
            self.text(x+w/2, y+h/2-(len(lines)-1)*13+i*26+7, line)
        self.parts.append('</g>')
    def arrow(self, pts: list[tuple[float,float]], color: str=INK):
        d = 'M ' + ' L '.join(f'{x} {y}' for x,y in pts)
        self.parts.append(f'<path data-connector="true" d="{d}" fill="none" stroke="{color}" stroke-width="2" marker-end="url(#arrow)"/>')
    def note(self, a: str, b: str=''):
        self.text(620, 685, a, 20)
        if b: self.text(620, 719, b, 18)
    def array(self, values: Sequence[object], y: int, label: str, active: tuple[int,...]=(), x: int=220, width: int=120):
        if label: self.text(620, y-36, label, 22)
        for i, v in enumerate(values):
            self.box(x+i*width, y, width-8, 60, [str(v)], GREEN if i in active else BLUE)
            self.text(x+i*width+(width-8)/2, y+85, i, 18)
    def chain(self, values: list[str], y: int, label: str, *, double: bool=False, circular: bool=False, highlights: tuple[int,...]=(), x: int=240):
        self.text(620, y-65, label, 22)
        for i,v in enumerate(values):
            xx=x+i*230
            self.box(xx,y,150,70,[v],GREEN if i in highlights else BLUE)
            if i<len(values)-1:
                self.arrow([(xx+150,y+23),(xx+230,y+23)])
                if double: self.arrow([(xx+230,y+50),(xx+150,y+50)],'#7c3aed')
        if not values:
            self.box(440,y,360,70,['head = tail = None'],ORANGE)
            return
        last=x+(len(values)-1)*230
        self.text(x+75,y-20,'head',18)
        self.arrow([(x+75,y-15),(x+75,y)])
        self.text(last+75,y+117,'tail',18)
        self.arrow([(last+75,y+96),(last+75,y+70)])
        if circular:
            self.arrow([(last+150,y+35),(last+185,y+35),(last+185,y+150),(x-35,y+150),(x-35,y+35),(x,y+35)],'#0f766e')
            self.text(1030,y+120,'tail.next = head',18,'#0f766e')
        else:
            self.arrow([(last+150,y+23),(last+195,y+23)])
            self.text(last+225,y+29,'None',18)
        if double:
            self.arrow([(x,y+50),(x-60,y+50)],'#7c3aed')
            self.text(x-100,y+57,'None',18)
    def svg(self, alt: str):
        return '<svg xmlns="http://www.w3.org/2000/svg" width="1240" height="760" viewBox="0 0 1240 760" role="img" aria-labelledby="title desc"><title id="title">'+html.escape(alt.split('.')[0])+'</title><desc id="desc">'+html.escape(alt)+'</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 Z" fill="'+INK+'"/></marker></defs><rect x="0" y="0" width="1240" height="760" fill="#ffffff"/>'+''.join(self.parts)+'</svg>\n'

# Tiny executable reference models validate the states rendered below.
class Node:
    def __init__(self, label: str):
        self.label = label
        self.next: Node | None = None
        self.prev: Node | None = None

def chain_model(labels: list[str], circular: bool=False, double: bool=False):
    nodes = [Node(v) for v in labels]
    for i,n in enumerate(nodes):
        n.next = nodes[i+1] if i+1<len(nodes) else nodes[0] if circular else None
        n.prev = nodes[i-1] if i>0 and double else None
    return nodes

def verify_chain(nodes: list[Node], expected: list[str], *, circular: bool=False, double: bool=False):
    assert [n.label for n in nodes] == expected
    for i,n in enumerate(nodes):
        assert n.next is (nodes[i+1] if i+1<len(nodes) else nodes[0] if circular else None)
        if double: assert n.prev is (nodes[i-1] if i else None)
    return {'values': expected, 'head': expected[0] if expected else None, 'tail': expected[-1] if expected else None, 'size':len(expected), 'circular':circular, 'reciprocal':double}

class SkipNode:
    def __init__(self, key: int, height: int):
        self.key = key
        self.forward: list[SkipNode | None] = [None] * height

class SkipModel:
    def __init__(self):
        self.head = SkipNode(-1, 3)
    def predecessors(self, target: int) -> tuple[list[SkipNode], list[tuple[str, int, int]]]:
        node = self.head
        update = [self.head] * 3
        trace = []
        for level in range(2, -1, -1):
            trace.append(('level',level,node.key))
            successor = node.forward[level]
            while successor is not None and successor.key < target:
                node = successor
                trace.append(('right',level,node.key))
                successor = node.forward[level]
            update[level] = node
        return update, trace
    def insert(self, key: int, height: int) -> tuple[list[int], list[tuple[str, int, int]]]:
        update, trace = self.predecessors(key)
        node = SkipNode(key,height)
        for level in range(height):
            node.forward[level] = update[level].forward[level]
            update[level].forward[level] = node
        return [n.key for n in update], trace
    def remove(self, key: int) -> bool:
        update, trace = self.predecessors(key)
        node = update[0].forward[0]
        if node is None or node.key != key: return False
        for level in range(len(node.forward)):
            assert update[level].forward[level] is node
            update[level].forward[level] = node.forward[level]
            node.forward[level] = None
        return True
    def rows(self) -> list[list[int]]:
        rows = []
        for level in range(3):
            row = []
            node = self.head.forward[level]
            while node is not None:
                row.append(node.key);node=node.forward[level]
            rows.append(row)
        return rows

placements=[]
for p in plan:
    key=p['lesson'].split('/')[1][3:]
    module=int(p['lesson'][:2])
    title=key.replace('-',' ').capitalize()
    d=Drawing(title, 'values are independent of the lesson exercise')
    alt=''
    check={}
    if key=='shallow-copies':
        a=[[3,8],[5]]; b=a.copy(); assert a is not b and a[0] is b[0]
        d.text(620,132,'After b = a.copy(): different outer lists, shared inner lists',22)
        for x,name in [(150,'a'),(650,'b')]:
            d.box(x,180,300,70,[name+' outer: slot 0 | slot 1'])
            d.arrow([(x+75,250),(x+75,300),(420,300),(420,340)])
            d.arrow([(x+225,250),(x+225,280),(870,280),(870,340)])
        d.box(320,340,200,70,['inner X: [3, 8]'],PURPLE)
        d.box(770,340,200,70,['inner Y: [5]'],PURPLE)
        b[0].append(9); assert a==[[3,8,9],[5]]
        d.arrow([(420,410),(420,485)])
        d.box(270,485,300,85,['b[0].append(9)','X becomes [3, 8, 9]'],GREEN)
        d.box(700,485,350,85,['a[0] is b[0]: True','both see the same change'],GREEN)
        d.note('Copying an empty list creates a distinct empty outer list.','Outer-slot arrows are references; the downward arrow below X shows a mutation, not a new object.')
        alt='Shallow copy: outer lists a and b point to the same inner lists X and Y. Appending 9 through b changes X to [3, 8, 9], visible through a too; outer lists remain distinct.'
        check={'a':a,'b':b,'outer_distinct':a is not b,'inner_shared':a[0] is b[0]}
    elif key=='auxiliary-space':
        a=[4,7,2,9]; low=high=a[0];states=[(low,high)]
        for v in a[1:]:low=min(low,v);high=max(high,v);states.append((low,high))
        assert states==[(4,4),(4,7),(2,7),(2,9)]
        d.array(a,170,'Input: four existing values (not auxiliary storage)')
        d.text(620,320,'One-pass extremes: working state after each value (low, high)',22)
        for i,state in enumerate(states):
            d.box(145+i*245,360,190,85,[f'value = {a[i]}',str(state)],PURPLE)
            if i<3:d.arrow([(335+i*245,402),(390+i*245,402)])
        d.box(350,530,540,75,['Return (2, 9); no copied input or growing output'],GREEN)
        d.note('Only low, high, seen and the current value are retained: O(1) working slots.','Bounded-size value model. Empty input returns None; a singleton 4 returns (4, 4).')
        alt='Extremes scan over unchanged input [4,7,2,9] keeps low/high pairs (4,4), (4,7), (2,7), (2,9). It returns (2,9) without copying the input; empty input returns None and a singleton returns its value twice.'
        check={'input':a,'states':states,'output':(low,high),'empty_output':None}
    elif key=='amortized-append':
        cap=0; n=0; total=0; costs=[]
        for v in range(1,9):
            c=1
            if n==cap: c+=n; cap=max(1,cap*2)
            n+=1;total+=c; costs.append(c)
        assert costs==[1,2,3,1,5,1,1,1] and total==15
        d.array(list(range(1,9)),170,'Append number (start empty)',x=130)
        d.array(costs,350,'Cost = copied references + one new write',active=(1,2,4),x=130)
        d.box(200,520,380,85,['8 appends: 15 total writes','average = 15 / 8 = 1.875'],GREEN)
        d.box(660,520,380,85,['capacity: 0 → 1 → 2 → 4 → 8','resize copies: 0 + 1 + 2 + 4'],ORANGE)
        d.note('Illustrative doubling model, NOT the exact Python-list growth policy.','A resize is expensive; the cost spread over many appends stays bounded per append.')
        alt='An explicit doubling model starts empty. Eight appends cost 1, 2, 3, 1, 5, 1, 1, 1 writes, totaling 15. Only full-capacity appends copy existing references.'
        check={'costs':costs,'total':total,'average':total/8,'capacity':cap}
    elif key in ('base-and-recursive-cases','recursive-sum','recursive-factorial'):
        if key=='base-and-recursive-cases':
            frames=['count(3): wait for 1 + count(2)','count(2): wait for 1 + count(1)','count(1): wait for 1 + count(0)','count(0): return 0 (base)']
            returns=['return 3','return 2','return 1','return 0']; note='Nonnegative integer contract: every call reduces n by one; n = 0 stops.'
            def count(n: int)->int: return 0 if n==0 else 1+count(n-1)
            assert count(3)==3 and count(0)==0;check={'count3':count(3),'count0':count(0)}
        elif key=='recursive-sum':
            frames=['sum_at(0): wait for 6 + sum_at(1)','sum_at(1): wait for 2 + sum_at(2)','sum_at(2): wait for 5 + sum_at(3)','sum_at(3): return 0 (i = length)']
            returns=['6 + 7 = 13','2 + 5 = 7','5 + 0 = 5','return 0'];note='Input [6, 2, 5] is unchanged. Index-based recursion: no slices are copied.'
            def sum_at(a: list[int],i: int=0)->int: return 0 if i==len(a) else a[i]+sum_at(a,i+1)
            assert sum_at([6,2,5])==13 and sum_at([])==0;check={'sum':13,'empty':0,'frames':4}
        else:
            frames=['fact(3): wait for 3 × fact(2)','fact(2): wait for 2 × fact(1)','fact(1): wait for 1 × fact(0)','fact(0): return 1 (base)']
            returns=['3 × 2 = 6','2 × 1 = 2','1 × 1 = 1','return 1']; note='Product lane shown; factorial_recursive(3) returns (6, 4): product 6 and four calls.'
            assert math.factorial(3)==6 and math.factorial(0)==1;check={'factorial3':6,'factorial0':1}
        d.text(400,135,'CALL DESCENT: suspended frames',22);d.text(970,135,'RETURN / UNWIND',22)
        for i,(f,r) in enumerate(zip(frames,returns)):
            y=170+i*115
            d.box(160+i*35,y,550,75,[f],GREEN if i==3 else BLUE)
            d.box(865,y,220,75,[r],GREEN)
            if i<3:
                d.arrow([(220+i*35,y+75),(220+i*35,y+115)])
                d.arrow([(1085,y+152),(1130,y+152),(1130,y+37),(1085,y+37)],'#0f766e')
        d.note(note,'Each suspended Python call has a frame; reaching the base case begins the return phase.')
        alt=title+': '+ '; '.join(frames)+'. Unwind: '+', '.join(reversed(returns))+'. '+note
    elif key=='fibonacci-tree':
        coords=[(550,125,'F(4) = 3'),(300,245,'F(3) = 2'),(800,245,'F(2) = 1'),(150,370,'F(2) = 1'),(450,370,'F(1) = 1'),(700,370,'F(1) = 1'),(950,370,'F(0) = 0'),(50,505,'F(1) = 1'),(250,505,'F(0) = 0')]
        for a,b in [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(3,7),(3,8)]:
            x,y,_=coords[a];xx,yy,_=coords[b];d.arrow([(x+75,y+65),(xx+75,yy)])
        for i,(x,y,label) in enumerate(coords):d.box(x,y,150,65,[label],ORANGE if i in (2,3) else GREEN if i in (4,5,6,7,8) else BLUE)
        def fib(n: int)->int:return n if n<2 else fib(n-1)+fib(n-2)
        assert fib(4)==3
        d.note('F(0) = 0; F(1) = 1. Both orange F(2) calls repeat the same work.','Value lane shown. fibonacci_tree(4) returns (3, 9): value 3 and nine calls, including base cases.')
        alt='Complete nine-call naive Fibonacci tree for F(4), returning 3. F(3) returns 2 and F(2) returns 1. Two orange F(2) subtrees repeat the same base-case work.'
        check={'result':fib(4),'calls':len(coords),'repeated_F2':2}
    elif key=='iterative-fibonacci':
        a,b=0,1; states=[(0,a,b)]
        for k in range(1,6):a,b=b,a+b;states.append((k,a,b))
        assert states==[(0,0,1),(1,1,1),(2,1,2),(3,2,3),(4,3,5),(5,5,8)]
        d.text(620,128,'Invariant after k steps: (a, b) = (F(k), F(k + 1))',22)
        for i,(k,a,b) in enumerate(states):
            x=110+(i%3)*370;y=185+(i//3)*225
            d.box(x,y,280,115,[f'k = {k}',f'a = {a}     b = {b}'],GREEN if k==5 else BLUE)
            if i%3<2:d.arrow([(x+280,y+57),(x+370,y+57)])
        d.arrow([(990,300),(990,345),(250,345),(250,410)])
        d.note('Simultaneous update: a, b = b, a + b uses BOTH old values.','fibonacci_loop(5) returns (5, 5): value and updates; n = 0 returns (0, 0). Fixed number of integer slots.')
        alt='Rolling Fibonacci state progresses (0,1), (1,1), (1,2), (2,3), (3,5), (5,8). After five simultaneous updates a is F(5)=5. No recursion or retained list of prior values is needed.'
        check={'states':states,'result':states[-1][1]}
    elif key=='recursive-binary-search':
        a=[2,5,8,11,14,17,20]; lo,hi=0,len(a); mid=-1; trace=[]
        while lo<hi:
            mid=(lo+hi)//2;trace.append([lo,hi,mid,a[mid]])
            if a[mid]==17:break
            if a[mid]<17:lo=mid+1
            else:hi=mid
        assert trace==[[0,7,3,11],[4,7,5,17]]
        d.array(a,180,'Sorted array; target = 17; indices below',active=(5,),x=190)
        d.box(180,355,410,90,['Frame 1: [lo, hi) = [0, 7)','mid = 3; a[3] = 11 < 17'])
        d.box(680,355,400,90,['Frame 2: [lo, hi) = [4, 7)','mid = 5; a[5] = 17'],GREEN)
        d.arrow([(590,400),(680,400)])
        d.box(410,535,420,70,['Return index 5 through both frames'],GREEN)
        d.note('Half-open bounds; right recursion uses mid + 1, never mid.','Empty interval lo == hi: return None. Empty input begins [0, 0); no array access.')
        alt='Recursive binary search for 17 in [2,5,8,11,14,17,20] probes index 3 in [0,7), then index 5 in [4,7), and returns 5. Empty intervals return None without reading a cell.'
        check={'trace':trace,'index':mid}
    elif key=='append-with-capacity':
        slots=[4,9,None,None];n=2;slots[n]=6;n+=1
        assert slots==[4,9,6,None] and n==3
        d.array([4,9,'unused','unused'],180,'Before: size = 2, capacity = 4')
        d.arrow([(516,265),(516,350)],'#0f766e');d.text(820,320,'write slot[size] = 6; then size += 1',20)
        d.array([4,9,6,'unused'],410,'After append(6): size = 3, capacity = 4',active=(2,))
        d.note('Only one slot is written; existing values do not move.','Teaching buffer model. Empty with spare capacity writes index 0; a full buffer must grow first.')
        alt='A teaching array buffer with capacity four contains 4 and 9. Appending 6 writes unused index 2 and changes size from two to three, leaving capacity and prior cells unchanged.'
        check={'slots':slots,'size':n,'capacity':len(slots)}
    elif key=='delete-and-compact':
        a=[4,9,6,2];removed=a.pop(1); assert a==[4,6,2] and removed==9
        d.array([4,9,6,2],180,'Before: remove index 1 (value 9)',active=(1,))
        d.arrow([(516,240),(396,410)],'#0f766e');d.arrow([(636,240),(516,410)],'#0f766e')
        d.array([4,6,2,'unused'],410,'',active=(1,2))
        d.box(790,310,350,90,['AFTER: shift 2 and 3 left','size: 4 → 3'],GREEN)
        d.note('Clear the now-unused last reference in a fixed-capacity teaching buffer.','Delete last: no shifts. Delete singleton: size becomes 0. Empty: index 0 is invalid.')
        alt='Deleting index 1 from [4,9,6,2] removes 9. References 6 and 2 shift one position left, then the last slot is cleared; size becomes three. Deleting the last element requires no shifts.'
        check={'removed':removed,'after':a,'shifts':2}
    elif key=='reverse-two-pointers':
        a=[3,7,4,8,2]; snapshots=[a.copy()]; l,r=0,len(a)-1
        while l<r:a[l],a[r]=a[r],a[l];l+=1;r-=1;snapshots.append(a.copy())
        assert snapshots==[[3,7,4,8,2],[2,7,4,8,3],[2,8,4,7,3]]
        for i,s in enumerate(snapshots): d.array(s,155+i*160,['Before: left = 0, right = 4','Swap endpoints; left = 1, right = 3','Swap inner pair; left = right = 2 → stop'][i],active=((0,4),(1,3),(2,))[i])
        d.note('Each swap fixes two positions; the middle value stays in place.','Empty: (left, right) = (0, -1). Singleton: (0, 0). Both perform zero swaps.')
        alt='Reverse [3,7,4,8,2] by swapping indices 0 and 4, then 1 and 3. States are [2,7,4,8,3] and [2,8,4,7,3]. Pointers meet at the unchanged middle value.'
        check={'snapshots':snapshots,'swaps':len(snapshots)-1}
    elif key=='sliding-window':
        a=[4,1,7,2,6]; sums=[sum(a[i:i+3]) for i in range(3)]; assert sums==[12,10,15]
        for i,s in enumerate(sums): d.array(a,155+i*160,[f'Window [0, 3): 4 + 1 + 7 = {s}',f'Slide to [1, 4): 12 − 4 + 2 = {s}',f'Slide to [2, 5): 10 − 1 + 6 = {s}'][i],active=tuple(range(i,i+3)))
        d.note('Width k = 3: subtract the leaving value, add the entering value. Best sum = 15.','Input is unchanged. Require 1 ≤ k ≤ len(values); empty input has no valid positive-width window.')
        alt='Three width-three windows over [4,1,7,2,6] have sums 12,10,15. Shifting subtracts 4 and adds 2, then subtracts 1 and adds 6. The maximum is 15; the array does not change.'
        check={'window_sums':sums,'best':max(sums)}
    elif key=='prefix-sums':
        a=[4,1,7,2];prefix=[0]
        for v in a:prefix.append(prefix[-1]+v)
        assert prefix==[0,4,5,12,14] and prefix[4]-prefix[1]==10
        d.array(a,165,'Input values: original array stays unchanged',x=280)
        d.array(prefix,345,'Build prefix: prefix[0] = 0; prefix[i + 1] = prefix[i] + a[i]',active=(1,4))
        d.box(290,530,660,75,['Query [1, 4): prefix[4] − prefix[1] = 14 − 4 = 10'],GREEN)
        d.note('The half-open query includes indices 1, 2, 3: 1 + 7 + 2 = 10.','Empty range [i, i) sums to 0; empty input has prefix [0]. Static prefixes must be updated after mutation.')
        alt='Building prefix sums for [4,1,7,2] gives [0,4,5,12,14]. Query [1,4) subtracts prefix[1] from prefix[4] to obtain 10; an empty range subtracts the same boundary from itself.'
        check={'prefix':prefix,'query':prefix[4]-prefix[1]}
    elif module==4 or key in ('doubly-linked-node','doubly-prepend','doubly-append','browser-history','circular-append','circular-remove'):
        double=key.startswith('doubly') or key=='browser-history';circular=key.startswith('circular')
        before=['A: 4','B: 9'];after=before.copy();n=chain_model(before,circular,double)
        step=''; edge=''; highlight=()
        if key=='node-and-link':
            before=['A: 4'];after=['A: 4','B: 9'];n=chain_model(before);b=Node('B: 9');n[0].next=b;n.append(b)
            step='Assign A.next = B; tail = B; B.next remains None. A and B are distinct objects.'
            edge='A value and a next reference are different fields. None means no successor.'
        elif key=='traverse-nodes':
            before=['A: 4','B: 9','C: 6'];after=before.copy();n=chain_model(before)
            step='cursor: A → B → C → None; visits: [4, 9, 6]. Links do not change.'
            edge='Start cursor at head; advance cursor = cursor.next. Empty list: zero visits.'
        elif key=='list-state':
            before=[];after=['A: 4'];n=chain_model(after)
            step='Empty → first node: head and tail both reference A; size: 0 → 1.'
            edge='Singleton: head is tail; tail.next is None. Empty: both endpoints are None.'
        elif key in ('prepend-node','doubly-prepend'):
            after=['N: 2']+before;n=chain_model(before,double=double);new=Node('N: 2');new.next=n[0]
            if double:n[0].prev=new
            n.insert(0,new);highlight=(0,)
            step='1. N.next = old head; '+('2. old head.prev = N; 3. head = N.' if double else '2. head = N. Tail stays B; size: 2 → 3.')
            edge='Empty prepend: head = tail = N; '+('N.prev = N.next = None.' if double else 'N.next = None; size: 0 → 1.')
        elif key in ('append-node','doubly-append','circular-append'):
            after=before+['N: 6'];n=chain_model(before,circular,double);new=Node('N: 6')
            if double:new.prev=n[-1]
            new.next=n[0] if circular else None;n[-1].next=new;n.append(new);highlight=(2,)
            step=('N.next = head; old tail.next = N; tail = N; size: 2 → 3.' if circular else ('N.prev = B; B.next = N; tail = N; size: 2 → 3.' if double else 'old tail.next = N; tail = N; head stays A; size: 2 → 3.'))
            edge='Empty append: head = tail = N; '+('N.next = N (self-loop).' if circular else ('N.prev = N.next = None.' if double else 'N.next = None; size: 0 → 1.'))
        elif key=='find-node':
            before=['A: 4','B: 9','C: 4'];after=before.copy();n=chain_model(before);highlight=(0,)
            step='Find value 4: test A first → return node A, not node C. No links change.'
            edge='Missing value: cursor reaches None → return None. Empty: return None immediately.'
        elif key=='remove-head':
            before=['A: 4','B: 9','C: 6'];after=before[1:];n=chain_model(before);removed=n.pop(0);removed.next=None
            step='Save A; head = A.next (B); detach A.next = None; return node A (value 4); size: 3 → 2.'
            edge='Singleton removal: head = tail = None; size = 0. Empty: raise IndexError (illustrative contract).'
        elif key=='remove-tail':
            before=['A: 4','B: 9','C: 6'];after=before[:-1];n=chain_model(before);removed=n.pop();n[-1].next=None
            step='Scan to predecessor B; B.next = None; tail = B; return node C (value 6); size: 3 → 2.'
            edge='Singleton removal clears both endpoints. Empty: raise IndexError (illustrative contract).'
        elif key=='doubly-linked-node':
            step='Forward: A.next = B. Backward: B.prev = A. Traversal leaves both links unchanged.'
            edge='head.prev = None; tail.next = None. A singleton has both links None.'
        elif key=='browser-history':
            before=['A: Home','B: Guide','C: Help'];after=['A: Home','B: Guide','D: Blog'];n=chain_model(before,double=True)
            new=Node('D: Blog');old=n.pop();old.prev=None;new.prev=n[-1];n[-1].next=new;n.append(new);highlight=(2,)
            step='Back from C to B; visit D: B.next = D; D.prev = B; current = tail = D.'
            edge='The forward branch C is discarded. At head, Back is a no-op; at tail, Forward is a no-op.'
        elif key=='circular-remove':
            before=['A: 4','B: 9','C: 6'];after=before[1:];n=chain_model(before,circular=True);removed=n.pop(0);n[-1].next=n[0];removed.next=None
            step='remove_first(4): head = B; tail.next = B; detach A; return node A; size: 3 → 2.'
            edge='Singleton match clears head and tail and breaks the loop. Empty or missing: return None; no changes.'
        else:raise AssertionError(key)
        check=verify_chain(n,after,circular=circular,double=double)
        d.chain(before,190,'BEFORE'+(' • current = C' if key=='browser-history' else ' • cursor = A' if key=='traverse-nodes' else ''),double=double,circular=circular)
        d.chain(after,440,'AFTER'+(' • current = D' if key=='browser-history' else ' • cursor = None' if key=='traverse-nodes' else ''),double=double,circular=circular,highlights=highlight)
        if key in ('remove-head','remove-tail','circular-remove'):
            d.box(925,435,260,80,[('A: 4' if key!='remove-tail' else 'C: 6'),'detached; next = None'],ORANGE)
        d.note(step,edge)
        alt=title+'. Before: '+(' → '.join(before) or 'empty')+'. After: '+(' → '.join(after) or 'empty')+'. '+step+' '+edge
    elif key.startswith('skip-'):
        # Fixed levels are explicit reproducible teaching data, not random samples.
        old=[[4,9,15,22],[9,22],[22]]
        after=[row.copy() for row in old]
        if key=='skip-insert':
            after[0].insert(2,12);after[1].insert(1,12)
        if key=='skip-remove':
            after[0].remove(9);after[1].remove(9)
        for row in after:assert row==sorted(row)
        assert set(after[2])<=set(after[1])<=set(after[0])
        def levels(rows: list[list[int]],base_y: int,label: str):
            d.text(620,base_y-38,label,22)
            positions={4:330,9:490,12:650,15:810,22:970}
            for level in (2,1,0):
                y=base_y+(2-level)*70
                d.text(78,y+39,f'L{level}',18)
                d.box(125,y,130,60,['HEAD'],ORANGE if key=='skip-search' and level>0 else PURPLE)
                previous=255
                for value in rows[level]:
                    xx=positions[value]
                    d.arrow([(previous,y+30),(xx,y+30)],'#0f766e' if value==12 or key=='skip-search' and (level,value) in ((1,9),(0,15)) else INK)
                    d.box(xx,y,120,60,[str(value)],GREEN if value==12 or key=='skip-search' and value==15 else ORANGE if key=='skip-search' and value==9 else BLUE)
                    previous=xx+120
                d.arrow([(previous,y+30),(1150,y+30)])
                d.text(1180,y+37,'∅',20)
        if key in ('skip-insert','skip-remove'):
            levels(old,145,'BEFORE • explicitly chosen levels')
            levels(after,405,'AFTER • size = '+str(len(after[0]))+'; tail = 22 (unchanged)')
            if key=='skip-insert':
                a='Insert 12 with height 2: update[0] = 9; update[1] = 9; level 2 stays unchanged.'
                b='L0: 9 → 12 → 15; L1: 9 → 12 → 22. Return True. First insertion also sets tail; duplicate returns False.'
            else:
                a='Remove 9: HEAD bypasses it at L1; 4 bypasses it at L0. Level 2 stays unchanged.'
                b='Return True; missing returns False. Remove only key: HEAD → ∅ at all levels; tail = None; size = 0.'
        else:
            levels(old,185,'Aligned towers: upper rows are sorted subsequences of L0')
            if key=='skip-search':
                d.arrow([(190,245),(190,255)],'#c2410c')
                d.arrow([(550,315),(550,325)],'#c2410c')
                d.box(160,475,920,95,['Search 15: HEAD L2 (22 too large) → drop to L1','HEAD → 9 (22 too large) → drop to L0 → 15 found'],GREEN)
                a='Move right only while next key is smaller than target; then descend.'
                b='Search changes no links. Empty: HEAD.next[0] is None → missing; 16 stops before 22 → missing.'
            else:
                d.box(160,475,920,95,['Heights: 4 has 1; 9 has 2; 15 has 1; 22 has 3','Same key in several rows means ONE node with several forward references'],PURPLE)
                a='Every key is on level 0; higher levels provide shortcuts, not additional stored keys.'
                b='Empty: all HEAD links are None. Singleton: its chosen-height tower ends at None on each level.'
        d.note(a,b)
        alt=title+'. Fixed level data before: L0 [4,9,15,22], L1 [9,22], L2 [22]. '+a+' '+b
        model=SkipModel()
        for value,height in [(4,1),(9,2),(15,1),(22,3)]:model.insert(value,height)
        assert model.rows()==old
        search_update,search_trace=model.predecessors(15)
        found=search_update[0].forward[0]
        assert found is not None and found.key==15
        assert search_trace==[('level',2,-1),('level',1,-1),('right',1,9),('level',0,9)]
        miss,_=model.predecessors(16)
        next_key=miss[0].forward[0]
        assert next_key is not None and next_key.key==22
        if key=='skip-insert':
            updates,_=model.insert(12,2)
            assert updates==[9,9,-1]
        if key=='skip-remove':assert model.remove(9)
        assert model.rows()==after
        assert not model.remove(99)
        empty=SkipModel();assert empty.rows()==[[],[],[]]
        empty.insert(7,2);assert empty.rows()==[[7],[7],[]]
        assert empty.remove(7) and empty.rows()==[[],[],[]]
        check={'before':old,'after':after,'levels_nested':True,'search15':search_trace,'missing16_next':22,'empty_singleton_roundtrip':True,'actual_pointer_rewiring':True}
    else:raise AssertionError(key)
    assert alt and check
    text=d.svg(alt)
    canonical=OUT/p['file'];canonical.write_text(text)
    local=ROOT/p['lesson'];local.mkdir(parents=True,exist_ok=True);(local/p['file']).write_text(text)
    assert canonical.read_bytes()==(local/p['file']).read_bytes()
    row={**p,'alt':alt,'caption':alt,'placement':'After the representation/invariant explanation and before the implementation task.','illustrative_data':True,'canonical_svg':str(canonical.relative_to(ROOT)),'canonical_editable':'assets/diagrams/'+p['editable'],'local_svg':p['lesson']+'/'+p['file'],'local_editable':p['lesson']+'/'+p['editable'],'lesson_available_at_initial_authoring':False,'svg_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest()}
    placements.append(row);checks[p['file']]=check

# Edge-case model suite, independent of visual text and run on every regeneration.
for circular,double in [(False,False),(False,True),(True,False)]:
    for before in [[],['A'],['A','B'],['A','B','C']]:
        for operation in ('prepend','append','remove_head','remove_tail'):
            nodes=chain_model(before,circular,double)
            if operation.startswith('remove') and not nodes:continue
            expected=before.copy()
            if operation=='prepend':
                q=Node('N');q.next=nodes[0] if nodes else q if circular else None
                if nodes and double:nodes[0].prev=q
                nodes.insert(0,q);expected.insert(0,'N')
                if circular:nodes[-1].next=q
            elif operation=='append':
                q=Node('N');q.next=nodes[0] if circular and nodes else q if circular else None
                if nodes:
                    nodes[-1].next=q
                    if double:q.prev=nodes[-1]
                nodes.append(q);expected.append('N')
            elif operation=='remove_head':
                removed=nodes.pop(0);expected.pop(0);removed.next=None;removed.prev=None
                if nodes:
                    if double:nodes[0].prev=None
                    if circular:nodes[-1].next=nodes[0]
            else:
                removed=nodes.pop();expected.pop();removed.next=None;removed.prev=None
                if nodes:nodes[-1].next=nodes[0] if circular else None
            verify_chain(nodes,expected,circular=circular,double=double)
checks['linked_edge_suite']='42 nonempty/empty insertion and removal model transitions passed'
assert sum(4 if n else 2 for n in [0,1,2,3])*3 == 42
SCRATCH.mkdir(parents=True,exist_ok=True)
(OUT/'placements-extra-01-05.json').write_text(json.dumps(placements,indent=2)+'\n')
(OUT/'audit-extra-01-05.json').write_text(json.dumps({'planned':len(plan),'generated_svg':len(placements),'trace_checks':checks,'native_acceptance':'Run build-extra-01-05.mjs','visual_review':'pending','scope':'Only modules 01–05 extra diagram filenames; no lesson.md edits'},indent=2)+'\n')
print(json.dumps({'svg_count':len(placements),'local_svg_count':len(placements),'model_edge_transitions':42,'output':str(OUT)}))
