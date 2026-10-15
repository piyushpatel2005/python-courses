#!/usr/bin/env python3
"""Original 500px teaching figures. Run here; native acceptance uses scratch dependencies.
SVGs are platform artifacts. Every array cell/node is native editable geometry.
The figures use illustrative fixtures, not assessment fixtures.
"""
from pathlib import Path
import json, html, hashlib, itertools, math
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'assets/diagrams'
PLAN = json.loads((ROOT/'assets/diagram-plan.json').read_text())[:20]
BLUE, GREEN, ORANGE, PURPLE, GRAY = '#dbeafe', '#dcfce7', '#ffedd5', '#ede9fe', '#f1f5f9'
INK = '#172033'
class Figure:
    def __init__(self, title, desc, height=460):
        self.title, self.desc, self.height = title, desc, height
        self.parts=[]; self.trace={}
        self.text(24, 32, title, 22)
    def text(self,x,y,s,size=16,anchor='start',color=INK):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" text-anchor="{anchor}" fill="{color}">{html.escape(str(s))}</text>')
    def box(self,x,y,w,h,s=None,fill=BLUE,size=16):
        self.parts.append(f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="#526279" stroke-width="1.5"/>')
        if s is not None: self.text(x+w/2,y+h/2+size*.35,s,size,'middle')
        self.parts.append('</g>')
    def arrow(self,*points,color='#526279'):
        d='M '+' L '.join(f'{x},{y}' for x,y in points)
        self.parts.append(f'<path data-connector="true" d="{d}" fill="none" stroke="{color}" stroke-width="1.8" marker-end="url(#arrow)"/>')
    def cells(self,vals,y,x=40,w=70,h=42,colors=None,indices=False):
        for i,v in enumerate(vals):
            self.box(x+i*w,y,w-4,h,v,(colors or {}).get(i,BLUE))
            if indices: self.text(x+i*w+(w-4)/2,y-9,i,14,'middle')
    def chain(self,vals,y,x=40,w=85,gap=55,colors=None,back=False):
        for i,v in enumerate(vals):
            xx=x+i*(w+gap); self.box(xx,y,w,42,v,(colors or {}).get(i,BLUE))
            if i:
                px=x+(i-1)*(w+gap)
                self.arrow((px+w,y+15 if back else y+21),(xx,y+15 if back else y+21))
                if back:self.arrow((xx,y+29),(px+w,y+29))
    def finish(self,caption):
        self.text(24,self.height-42,caption,14)
        self.text(24,self.height-20,'Illustrative data • not the exercise input',14,color='#475569')
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="500" height="{self.height}" viewBox="0 0 500 {self.height}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(self.title)}</title><desc id="desc">{html.escape(self.desc)}</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#526279"/></marker></defs><rect width="500" height="{self.height}" fill="#ffffff"/>'+''.join(self.parts)+'</svg>\n'
def main():
    figs=[]
    def keep(f,caption,trace): figs.append((f,caption,trace))

    f=Figure('Alias or rebind?', 'Before rebinding, names a and b both refer to list [17]. After a is rebound to [29], b still refers to the original list [17].',430)
    f.text(24,70,'Before: b = a')
    f.box(40,92,65,40,'a');f.box(40,153,65,40,'b');f.box(285,112,150,55,'[17]',GREEN)
    f.arrow((105,112),(190,112),(190,130),(285,130));f.arrow((105,173),(218,173),(218,150),(285,150))
    f.text(24,231,'After: a = [29]')
    f.box(40,253,65,40,'a');f.box(40,314,65,40,'b');f.box(285,253,150,40,'[29]',ORANGE);f.box(285,314,150,40,'[17]',GREEN)
    f.arrow((105,273),(285,273));f.arrow((105,334),(285,334))
    a=[17];b=a;a=[29];assert a is not b and b==[17]
    keep(f,'Arrows mean references, not copied values.',{'a':a,'b':b,'same_object_after':a is b})

    f=Figure('Where a shallow copy stops','Two distinct outer lists point to the same inner list [17, 23]. Copying each inner list creates independent inner lists; changing the copied inner list does not alter the original.',480)
    f.text(24,70,'Shallow: two outer lists, one inner list')
    f.box(35,95,130,45,'outer[0]');f.box(35,165,130,45,'copy[0]');f.box(300,130,155,45,'[17, 23]',GREEN)
    f.arrow((165,117),(225,117),(225,144),(300,144));f.arrow((165,187),(250,187),(250,162),(300,162))
    f.text(24,258,'Copy the inner list as well')
    f.box(35,285,130,45,'outer[0]');f.box(300,285,155,45,'[17, 23]',GREEN);f.arrow((165,307),(300,307))
    f.box(35,355,130,45,'copy[0]');f.box(300,355,155,45,'[17, 99]',ORANGE);f.arrow((165,377),(300,377))
    outer=[[17,23]];shallow=outer.copy();independent=[row.copy() for row in outer];independent[0][1]=99
    assert shallow is not outer and shallow[0] is outer[0] and independent[0] is not outer[0]
    keep(f,'Lower panel: change only copy[0][1] to 99.',{'outer':outer,'independent':independent,'shallow_inner_shared':shallow[0] is outer[0]})

    f=Figure('Count work, not elapsed time','Exact operation counts for input sizes 4, 8, 16, and 32: one visit per item, repeated integer halving until 1, and one visit per distinct unordered pair.',430)
    f.text(30,80,'Input n',16);f.text(152,80,'Visits',16);f.text(255,80,'Halvings',16);f.text(381,80,'Pairs',16)
    counts=[]
    for i,n in enumerate([4,8,16,32]):
        k=n;h=0
        while k>1:k//=2;h+=1
        p=sum(1 for _ in itertools.combinations(range(n),2)); counts.append([n,n,h,p])
        f.cells([n,n,h,p],103+i*50,x=28,w=115,h=40,colors={0:GRAY,1:BLUE,2:GREEN,3:ORANGE})
    f.text(28,330,'Visits: n     Halvings: stop when n = 1',14)
    f.text(28,354,'Pairs: count each i < j once; n(n − 1)/2',14)
    keep(f,'Equal-cost counted steps; these are not timings.',{'columns':['n','visits','halvings','pairs'],'rows':counts})

    f=Figure('Calls descend; returns unwind','A countdown called with 2 calls 1, then 0. Zero is the base case. All calls return None, unwinding from 0 to 1 to 2.',470)
    f.text(40,78,'CALLS',16);f.text(300,78,'RETURNS',16)
    for i,n in enumerate([2,1,0]):
        y=100+i*90;f.box(35,y,145,48,f'count({n})',GREEN if n==0 else BLUE)
        f.box(285,y,180,48,f'{n} returns None',GREEN if n==0 else PURPLE)
        if i<2:f.arrow((107,y+48),(107,y+90));f.arrow((375,y+90),(375,y+48))
    f.arrow((180,304),(285,304));f.text(35,368,'At 0: no child call; start returning.',16)
    trace=[]
    def count(n):
        trace.append(['call',n])
        if n:count(n-1)
        trace.append(['return',n,None])
    count(2)
    keep(f,'Definition: recurse only while n > 0.',trace)

    f=Figure('Repeated calls versus cached values','The naive Fibonacci call tree for f(4) has nine calls, including two f(2) calls. With base values f(0)=0 and f(1)=1 cached, compute f(2)=1, f(3)=2, and f(4)=3 once each.',580)
    f.text(24,66,'Naive tree: f(n), not return values',14)
    positions=[(220,85,'f(4)'),(115,165,'f(3)'),(360,165,'f(2)'),(50,245,'f(2)'),(200,245,'f(1)'),(320,245,'f(1)'),(420,245,'f(0)'),(20,325,'f(1)'),(110,325,'f(0)')]
    for p,c in [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(3,7),(3,8)]:
        x,y,_=positions[p];xx,yy,_=positions[c];f.arrow((x+30,y+38),(xx+30,yy))
    for x,y,s in positions:f.box(x,y,60,38,s,ORANGE if s=='f(2)' else BLUE)
    f.text(24,411,'Memoized: reuse stored f(2) = 1',16)
    f.cells(['f(0)','f(1)','f(2)','f(3)','f(4)'],435,x=25,w=90,h=34)
    f.cells([0,1,1,2,3],474,x=25,w=90,h=34,colors={i:GREEN for i in range(5)})
    calls=[]
    def fib(n):
        calls.append(n);return n if n<2 else fib(n-1)+fib(n-2)
    r=fib(4);assert r==3 and len(calls)==9
    cache={0:0,1:1};hits=[]
    def memo(n):
        if n in cache:hits.append(n);return cache[n]
        cache[n]=memo(n-1)+memo(n-2);return cache[n]
    assert memo(4)==r
    keep(f,'Bases: f(0)=0, f(1)=1; recurrence adds two children.',{'naive_calls':calls,'result':r,'cache_values':[cache[i] for i in range(5)],'cache_hits':hits})

    f=Figure('Make room without losing a value','Insert 19 at index 1 into a capacity-four buffer containing 13, 27, 41. First copy index 2 to 3, then 1 to 2, then write 19 at 1 and increase size from 3 to 4.',535)
    buf=[13,27,41,None];states=[buf.copy()]
    for j in [2,1]:buf[j+1]=buf[j];states.append(buf.copy())
    buf[1]=19;states.append(buf.copy())
    labels=['Before: size 3, capacity 4','1. Copy index 2 to 3','2. Copy index 1 to 2','3. Write 19 at 1; size becomes 4']
    for i,(s,label) in enumerate(zip(states,labels)):
        y=100+i*100;f.text(30,y-30,label,16);f.cells(['·' if v is None else v for v in s],y,x=45,w=100,indices=True,colors={3 if i==1 else 2 if i==2 else 1:ORANGE} if i else {3:GRAY})
    keep(f,'Shift right to left; duplicates during copying are OK.',{'states':states,'final_size':4,'capacity':4})

    f=Figure('Prefix sums subtract a boundary','Values [3, 8, 2, 6] have prefix sums [0, 3, 11, 13, 19]. Range [1, 3) includes values 8 and 2. Subtract prefix[1] from prefix[3] to get 10.',405)
    v=[3,8,2,6];p=[0]+list(itertools.accumulate(v));l,r=1,3
    f.text(25,75,'Values: select [1, 3)',16);f.cells(v,110,x=45,w=100,indices=True,colors={1:GREEN,2:GREEN})
    f.text(25,205,'Prefix: sum of values strictly before index',16);f.cells(p,240,x=25,w=90,indices=True,colors={1:ORANGE,3:ORANGE})
    f.text(35,324,f'prefix[3] − prefix[1] = {p[r]} − {p[l]} = {p[r]-p[l]}',18)
    keep(f,'Left included, right excluded; prefix[0] = 0.',{'values':v,'prefix':p,'range':[l,r],'sum':p[r]-p[l]})

    f=Figure('Splice after a known node','Initially A links to C. First save C by setting new node B.next to A.next while A still links to C. Then set A.next to B, creating A to B to C.',590)
    f.text(24,72,'Before: A.next is C',16);f.chain(['A','C'],95,x=40,w=85,gap=195)
    f.text(24,194,'1. B.next = A.next   (preserve C)',16)
    f.box(40,219,85,42,'A');f.box(320,219,85,42,'C');f.box(180,300,85,42,'B',ORANGE)
    f.arrow((125,240),(320,240));f.arrow((265,321),(362,321),(362,261))
    f.text(24,407,'2. A.next = B',16);f.chain(['A','B','C'],434,colors={1:ORANGE})
    f.text(24,511,'C.next is unchanged in every panel.',14)
    links={'A':'C','C':None};links['B']=links['A'];mid=links.copy();links['A']='B'
    keep(f,'New node B exists before either link assignment.',{'intermediate':mid,'after':links})

    f=Figure('Bypass; then fix boundary pointers','Removing middle B changes A.next to C. If removing the head, head becomes its next node. If removing the tail, tail becomes its predecessor. Removing the only node sets both head and tail to None.',650)
    f.text(24,72,'Middle removal: target B',16);f.chain(['A','B','C'],95,colors={1:ORANGE})
    f.text(24,180,'After: A.next = C',16);f.chain(['A','C'],202,x=40,w=85,gap=195)
    f.text(24,300,'Head case: remove A from A → C',16);f.box(40,323,85,42,'head',PURPLE);f.box(320,323,85,42,'C',GREEN);f.arrow((125,344),(320,344))
    f.text(24,421,'Tail case: remove C from A → C',16);f.box(40,444,85,42,'tail',PURPLE);f.box(320,444,85,42,'A',GREEN);f.arrow((125,465),(320,465))
    f.text(24,553,'Only node removed: head = tail = None',16)
    cases={}
    for label,values,target in [('middle',['A','B','C'],'B'),('head_case',['A','C'],'A'),('tail_case',['A','C'],'C'),('singleton',['A'],'A')]:
        links=dict(zip(values,values[1:]+[None]));head=values[0];tail=values[-1];prev=None;current=head
        while current!=target:
            assert current is not None
            prev,current=current,links[current]
        assert current is not None
        if prev is None:head=links[current]
        else:links[prev]=links[current]
        if current==tail:tail=prev
        links[current]=None
        remaining=[];cursor=head
        while cursor is not None:remaining.append(cursor);cursor=links[cursor]
        cases[label]={'remaining':remaining,'head':head,'tail':tail,'links':links}
    assert cases['middle']['remaining']==['A','C'] and cases['singleton']['head'] is cases['singleton']['tail'] is None
    keep(f,'Nonempty tail must have next = None.',cases)

    f=Figure('Reverse one link; keep the suffix','Before one reversal iteration, prev is A, current is B, and saved next is C. A.next is None and B.next is C. After setting B.next to A and advancing, prev is B and current is C; the suffix beginning at C remains reachable.',530)
    f.text(24,72,'Before: save next = current.next',16)
    for x,s in [(40,'prev'),(180,'current'),(320,'next')]:f.text(x,112,s,16)
    f.box(40,130,85,42,'A');f.box(180,130,85,42,'B',ORANGE);f.box(320,130,85,42,'C',GREEN);f.arrow((265,151),(320,151))
    f.text(40,202,'A.next = None',14);f.text(180,232,'B.next = C',14)
    f.text(24,294,'After: B.next = A; advance both pointers',16)
    for x,s in [(180,'prev'),(320,'current')]:f.text(x,336,s,16)
    f.box(40,353,85,42,'A');f.box(180,353,85,42,'B',ORANGE);f.box(320,353,85,42,'C',GREEN);f.arrow((180,374),(125,374))
    f.text(40,425,'A.next = None',14);f.text(24,463,'Saved C is now current; its links are untouched.',14)
    links={'A':None,'B':'C','C':None};prev,cur='A','B';nxt=links[cur];links[cur]=prev;prev,cur=cur,nxt
    keep(f,'Only the current node’s next link changes this turn.',{'links':links,'prev':prev,'current':cur,'saved_next':nxt})

    f=Figure('Reconnect both directions','Before deletion, A and B and C have reciprocal next and prev links. Removing middle node B sets A.next to C and C.prev to A; B is detached by clearing both of its links.',460)
    f.text(24,74,'Before: next → above; ← prev below',16);f.chain(['A','B','C'],100,back=True,colors={1:ORANGE})
    f.text(24,209,'After: A.next = C; C.prev = A',16);f.chain(['A','C'],238,x=40,w=85,gap=195,back=True)
    f.box(180,332,85,42,'B',GRAY);f.text(24,399,'Detached B: prev = next = None',16)
    nxt={'A':'B','B':'C','C':None};prv={'A':None,'B':'A','C':'B'};victim='B'
    left,right=prv[victim],nxt[victim];nxt[left]=right;prv[right]=left;nxt[victim]=prv[victim]=None
    assert nxt['A']=='C' and prv['C']=='A'
    keep(f,'Middle-node case; head and tail stay unchanged.',{'next':nxt,'prev':prv})

    f=Figure('A ring stops on identity, not None','A circular list has head A, then B, then C whose next points back to A. Visit A, B, C once and stop before revisiting head A. A conventional linear list instead ends at None.',510)
    f.text(40,82,'head',16);f.arrow((68,91),(68,120));f.chain(['A','B','C'],120)
    f.arrow((405,141),(451,141),(451,226),(68,226),(68,162))
    f.text(24,280,'One lap: visit A, B, C; stop at A again.',16)
    f.text(24,327,'Linear list: None ends traversal',16);f.chain(['A','B','None'],352,colors={2:GRAY})
    links={'A':'B','B':'C','C':'A'};vis=[];cur='A'
    while True:
        vis.append(cur);cur=links[cur]
        if cur=='A':break
    keep(f,'Nonempty ring; compare node identity to head.',{'ring':links,'one_lap':vis,'stop_at':cur})

    f=Figure('Search along lanes, then drop','A skip list has sorted base keys 7, 18, 31, 46. Search for 26 begins at the head on level 1, moves right to 18, rejects the forward key 46 as too large, then drops to level 0. The next key 31 is too large, so the predecessor is 18 on both levels.',460)
    f.text(24,73,'Target 26: advance only to keys < 26',16)
    f.text(24,110,'Level 1',14);f.box(30,130,62,42,'head',GRAY);f.box(200,130,62,42,'18',GREEN);f.box(390,130,62,42,'46')
    f.arrow((92,151),(200,151));f.arrow((262,151),(390,151));f.arrow((231,172),(231,272))
    f.text(24,252,'Level 0',14)
    xs=[30,115,200,295,390];vals=['head',7,18,31,46]
    for i,(x,v) in enumerate(zip(xs,vals)):
        f.box(x,272,62,42,v,GREEN if v==18 else GRAY if v=='head' else BLUE)
        if i:f.arrow((xs[i-1]+62,293),(x,293))
    f.text(24,356,'Trace: head → 18; drop; stop before 31.',16)
    f.text(24,393,'Predecessors: level 1 = 18, level 0 = 18',16)
    levels=[[7,18,31,46],[18,46]];target=26;current=None;moves=[]
    preds: list[int | None]=[None,None]
    for level in [1,0]:
        for key in levels[level]:
            if current is not None and key<=current:continue
            if key>=target:break
            current=key;moves.append(['right',level,key])
        preds[level]=current
        if level:moves.append(['drop',current])
    assert preds==[18,18]
    keep(f,'Fixed illustrative levels; vertical move keeps key.',{'levels':levels,'target':target,'predecessors':preds,'moves':moves})

    f=Figure('The most recent value leaves first','A stack initially contains bottom 14 and top 28. Pushing 35 puts it above 28. Popping returns 35 and restores top 28.',450)
    for x,label in [(30,'Before'),(190,'push(35)'),(350,'pop()')]:f.text(x,80,label,16)
    for x,vals in [(30,[14,28]),(190,[14,28,35]),(350,[14,28])]:
        for i,v in enumerate(vals):f.box(x,300-i*52,120,42,v,ORANGE if v==35 else BLUE)
        top_y=300-(len(vals)-1)*52;f.text(x,top_y-15,'top',16)
    f.text(30,382,'pop() returns 35; stored order is restored.',16)
    s=[14,28];s.append(35);pushed=s.copy();returned=s.pop()
    keep(f,'Bottom drawn low; only the top is added/removed.',{'pushed':pushed,'returned':returned,'after':s})

    f=Figure('Store the closer you expect','For ([ ]), scanning opening parenthesis and opening bracket pushes expected closers ) then ]. Closing bracket pops ], and closing parenthesis pops ), leaving empty. For ([), the closing parenthesis mismatches top ], so reject immediately.',590)
    f.text(24,75,'Valid input: ([])',18)
    f.text(30,112,'Read',14);f.text(170,112,'Expected closers (top at right)',14)
    stack=[];tr=[]
    for i,c in enumerate('([])'):
        if c in '([':stack.append({'(':')','[':']'}[c])
        else:assert stack.pop()==c
        tr.append(stack.copy());y=130+i*65;f.box(30,y,70,40,c,GRAY)
        if stack:f.cells(stack,y,x=175,w=65,h=40,colors={len(stack)-1:ORANGE})
        else:f.text(175,y+27,'empty: balanced',16)
    f.text(24,430,'Mismatch input: ([)',18)
    f.box(30,451,70,40,')',GRAY);f.cells([')',']'],451,x=175,w=65,h=40,colors={1:ORANGE})
    f.text(24,524,'Read ) but top expects ]: reject, do not pop.',16)
    mismatch_stack=[];expected=None;actual=None
    for c in '([)':
        if c in '([':mismatch_stack.append({'(':')','[':']'}[c])
        elif mismatch_stack[-1]!=c:expected=mismatch_stack[-1];actual=c;break
        else:mismatch_stack.pop()
    assert expected==']' and actual==')'
    keep(f,'Only bracket characters shown; stack stores closers.',{'valid':'([])','stacks':tr,'mismatch':'([)','expected':expected,'actual':actual,'stack_at_reject':mismatch_stack})

    f=Figure('Dequeue at head; clear the last tail','Initially queue nodes 16 and 24 are head and tail. Dequeue returns 16, leaving both head and tail pointing to 24. A second dequeue returns 24 and sets both pointers to None.',540)
    f.text(24,72,'Before: 16 was enqueued first',16);f.text(40,111,'head',16);f.text(320,111,'tail',16);f.chain([16,24],130,x=40,w=85,gap=195)
    f.text(24,236,'dequeue() returns 16',16);f.box(40,261,100,40,'head',PURPLE);f.box(350,261,100,40,'tail',PURPLE);f.box(210,325,80,42,24,GREEN)
    f.arrow((90,301),(90,346),(210,346));f.arrow((400,301),(400,346),(290,346))
    f.text(24,425,'Next dequeue returns 24: queue is empty.',16);f.text(24,467,'head = tail = None; size = 0',18)
    q=[16,24];first=q.pop(0);mid=q.copy();last=q.pop(0)
    keep(f,'Linked queue: the last remaining node has next=None.',{'first_return':first,'middle':mid,'last_return':last,'after':q})

    f=Figure('Wrap the index, not the FIFO order','A ring buffer of capacity five has head 3 and size 3, storing 41 at index 3, 52 at 4, and 63 at 0. Enqueue 74 writes index (3+3) modulo 5 = 1, and size becomes 4. Logical order is 41, 52, 63, 74.',480)
    f.text(24,74,'Before: head = 3, size = 3, capacity = 5',16)
    f.cells([63,'·','·',41,52],115,x=25,w=90,indices=True,colors={1:GRAY,2:GRAY,3:GREEN})
    f.text(24,201,'Write index = (head + size) % capacity',16)
    f.text(24,232,'(3 + 3) % 5 = 1; enqueue 74',18)
    f.cells([63,74,'·',41,52],280,x=25,w=90,indices=True,colors={1:ORANGE,2:GRAY,3:GREEN})
    f.text(24,363,'After: head = 3, size = 4',16);f.text(24,400,'FIFO order: 41 → 52 → 63 → 74',18)
    buf=[63,None,None,41,52];head=3;size=3;idx=(head+size)%len(buf);buf[idx]=74;size+=1
    keep(f,'· = unused slot; head marks the next removal.',{'buffer':buf,'head':head,'size':size,'write_index':idx,'fifo':[buf[(head+i)%5] for i in range(size)]})

    f=Figure('A deque keeps only useful candidates','For values 9, 4, 6, 7 and window size 3, the first window has candidate indices 0 and 2. Advancing the window expires index 0 from the front. Incoming 7 removes weaker 6 at index 2 from the back. Append index 3, which is the new maximum.',580)
    f.text(24,74,'Window width 3; store indices, not values',16);f.cells([9,4,6,7],110,x=45,w=100,indices=True,colors={0:GREEN,1:GREEN,2:GREEN,3:ORANGE})
    f.text(24,208,'Before: window [0, 3), candidates',16);f.cells(['0:9','2:6'],230,x=55,w=110);f.text(55,294,'front = maximum',14)
    f.text(24,341,'Advance to [1, 4): expire 0 from front',16);f.cells(['2:6'],363,x=55,w=110)
    f.text(24,443,'7 removes 2:6 at back; append index 3',16);f.cells(['3:7'],465,x=55,w=110,colors={0:GREEN})
    from collections import deque
    v=[9,4,6,7];d=deque();trace=[]
    for i,value in enumerate(v):
        expired=[];weaker=[]
        while d and d[0]<=i-3:expired.append(d.popleft())
        while d and v[d[-1]]<=value:weaker.append(d.pop())
        d.append(i);trace.append({'i':i,'expired':expired,'weaker':weaker,'deque':list(d)})
    keep(f,'Cells read index:value; remove ties from back too.',{'values':v,'width':3,'trace':trace})

    f=Figure('A collision does not merge keys','Using sum of Unicode code points modulo four, keys ab and ba both hash to bucket 3. The bucket keeps separate entries ab:12 and ba:90; equality checks distinguish them.',470)
    f.text(24,74,'Teaching hash: sum(ord(c) for c in key) % 4',16)
    f.text(24,107,'"ab": (97 + 98) % 4 = 3',16);f.text(24,136,'"ba": (98 + 97) % 4 = 3',16)
    for i in range(4):
        y=177+i*55;f.box(30,y,55,38,i,GRAY)
        if i<3:f.text(115,y+26,'empty',16)
    f.box(180,342,105,38,'ab : 12',BLUE);f.box(355,342,110,38,'ba : 90',GREEN)
    f.arrow((85,361),(180,361));f.arrow((285,361),(355,361))
    f.text(24,411,'Lookup "ba": skip unequal "ab", then match.',16)
    h=lambda s:sum(map(ord,s))%4
    keep(f,'Illustrative hash only; not Python’s string hash.',{'buckets':{s:h(s) for s in ['ab','ba']},'entries':[['ab',12],['ba',90]]})

    f=Figure('A tombstone keeps the probe alive','With capacity five, linear probing, and integer hash k modulo five, keys 7, 12, and 17 occupy slots 2, 3, and 4. Deleting 12 leaves a tombstone in slot 3. Lookup of 17 checks 2, continues through 3, and matches 4. A miss for 22 continues to never-used slot 0 and stops.',570)
    f.text(24,75,'h(k) = k % 5; linear probing; capacity 5',16)
    f.text(24,112,'Before deletion',16);f.cells(['empty','empty',7,12,17],147,x=25,w=90,indices=True)
    f.text(24,238,'After deleting key 12',16);f.cells(['empty','empty',7,'DEL',17],273,x=25,w=90,indices=True,colors={0:GRAY,1:GRAY,3:ORANGE,4:GREEN})
    f.text(24,364,'Find 17: slot 2 → slot 3 → slot 4: found',16)
    f.text(24,407,'Find 22: 2 → 3 → 4 → 0: stop at empty',16)
    f.text(24,462,'DEL: continue. Never-used empty: stop.',16)
    f.text(24,495,'Replacing DEL with empty would hide key 17.',14)
    buf: list[int | str | None]=[None]*5
    for key in [7,12,17]:
        slot=key%5
        while buf[slot] is not None:slot=(slot+1)%5
        buf[slot]=key
    assert buf==[None,None,7,12,17]
    buf[buf.index(12)]='DEL'
    def lookup(k):
        seen=[]
        for j in range(5):
            i=(k+j)%5;seen.append(i)
            if buf[i] is None:return {'visited':seen,'found':False}
            if buf[i]==k:return {'visited':seen,'found':True}
    keep(f,'Empty means never used; DEL means deleted.',{'buffer':buf,'find17':lookup(17),'find22':lookup(22)})

    assert len(figs)==len(PLAN)==20
    placements=[]
    for entry,(fig,caption,trace) in zip(PLAN,figs):
        svg=fig.finish(caption);canonical=OUT/entry['file'];canonical.write_text(svg)
        local=ROOT/entry['lesson']/entry['file'];local.parent.mkdir(parents=True,exist_ok=True);local.write_bytes(canonical.read_bytes())
        placements.append({**entry,'alt':fig.desc,'caption':caption,'context_suggestion':'Place after introducing the representation and before the implementation task. Treat the labeled illustrative data as a separate worked trace, not as exercise expected output.','canonical_svg':str(canonical.relative_to(ROOT)),'local_svg':str(local.relative_to(ROOT)),'canonical_editable':str((OUT/entry['editable']).relative_to(ROOT)),'local_editable':str((local.parent/entry['editable']).relative_to(ROOT)),'computed_trace':trace,'svg_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest()})
    (OUT/'placements-first-half.json').write_text(json.dumps(placements,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'diagrams':len(figs),'svg_files':len(figs)*2,'placements':str(OUT/'placements-first-half.json')}))

if __name__ == "__main__":
    main()
