#!/usr/bin/env python3
"""Generate only the 35 additional module 06–10 figures; original illustrative data.
Run Python, then build-extra-06-10.mjs for native real-editor acceptance.
No lesson prose or shared helper is modified. Sorting variants are explicitly named.
"""
from pathlib import Path
import importlib.util, json, hashlib, bisect
from collections import deque
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'assets/diagrams'
spec=importlib.util.spec_from_file_location('figure_helper',OUT/'build-first-half.py')
assert spec is not None and spec.loader is not None
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
Figure=mod.Figure
BLUE,GREEN,ORANGE,PURPLE,GRAY=mod.BLUE,mod.GREEN,mod.ORANGE,mod.PURPLE,mod.GRAY
PLAN=[p for p in json.loads((ROOT/'assets/additional-diagram-plan.json').read_text()) if 6<=int(p['lesson'][:2])<=10]
SCENES={}
def row(label,values,note='',hot=(),chain=False,indices=True):
    return dict(label=label,values=list(values),note=note,hot=list(hot),chain=chain,indices=indices)
def add(slug,title,rows,caption,checks):
    assert slug not in SCENES
    SCENES[slug]=dict(title=title,rows=rows,caption=caption,checks=checks)
def hash_index(s,m):
    h=0
    for c in s:h=(31*h+ord(c))%m
    return h

def build():
    a=[];b=[];a.append(17);assert b==[] and a is not b
    add('stack-state','Separate stacks, separate storage',[
        row('Before: new A and new B each own []',[], 'No top exists; len(A) = len(B) = 0.'),
        row('After A.push(17): A.items',a,'A top = index 0; len(A) = 1.',[0]),
        row('B.items remains empty',b,'B has no top; len(B) = 0.')],
        'The list end is the top; there are no head/tail fields.',{'a':a,'b':b,'distinct_lists':a is not b})
    a=[17,29];before=a.copy();ret=a.append(43);assert a==[17,29,43] and ret is None
    add('push-item','Push extends the top',[
        row('Before: bottom → top',before,'Top index 1 = 29; length 2.',[1]),
        row('push(43) returns None',a,'After: top index 2 = 43; length 3.',[2]),
        row('Empty case: [] → push(17)',[17],'Top index 0; length 0 → 1.',[0])],
        'Existing items keep their indices and order.',{'before':before,'after':a,'returned':ret,'empty_push':[17]})
    a=[17,29,43];before=a.copy();ret=a[-1];assert ret==43 and a==before
    add('peek-item','Peek reads; it does not pop',[
        row('Before peek(): bottom → top',before,'Top index 2; length 3.',[2]),
        row('Returned value', [ret],'Read items[-1]; no slot is removed.',[0],indices=False),
        row('After peek(): identical storage',a,'Top index 2; length 3; same list and items.',[2])],
        'Empty stack: raise IndexError, not a None marker.',{'before':before,'returned':ret,'after':a,'unchanged':a==before})
    stack=[];rows=[]
    for t in ['12','5','-','3','*']:
        if t in '-*':
            right=stack.pop();left=stack.pop();v=left-right if t=='-' else left*right;stack.append(v);note=f'Pop right {right}, then left {left}; push {v}.'
        else:stack.append(int(t));note='Bottom → top; last slot is top.'
        rows.append(row('Read token '+t,stack,note,[len(stack)-1]))
    assert stack==[21]
    add('postfix-evaluation','Postfix: operand order matters',rows,'Final one-item stack gives result 21.',{'tokens':['12','5','-','3','*'],'result':stack[0]})
    hist=['ink','ink+line'];text='ink+line+dot';rows=[row('Before: current text = ink+line+dot',hist,'Saved text states, oldest → newest.',[1])]
    text=hist.pop();rows.append(row('undo() returns True; text = ink+line',hist,'Pop the latest saved state; do not save again.',[0]))
    text=hist.pop();rows.append(row('undo() returns True; text = ink',hist,'History is now empty.'))
    assert text=='ink' and hist==[]
    rows.append(row('Next undo() returns False',hist,'Current text remains ink; no mutation.'))
    add('undo-history','Undo restores a saved state',rows,'A saved empty string is valid, not an empty stack.',{'final_text':text,'final_history':hist,'returns':[True,True,False]})
    entries=[];rows=[]
    for v in [9,4,4]:
        entries.append((v,min(v,entries[-1][1]) if entries else v))
    rows.append(row('Before: (value, minimum so far)',[f'{a},{b}' for a,b in entries],'Each pair summarizes its entire prefix.',[2]))
    entries.append((7,min(7,entries[-1][1])));rows.append(row('push(7): store (7, 4)',[f'{a},{b}' for a,b in entries],'minimum() returns 4; push returns None.',[3]))
    assert entries.pop()[0]==7;assert entries.pop()[0]==4
    rows.append(row('Pop 7, then pop one 4',[f'{a},{b}' for a,b in entries],'The other 4 remains; minimum() is still 4.',[1]))
    assert entries[-1][1]==4
    add('minimum-stack','A minimum saved at each depth',rows,'Cells show value,minimum; duplicate minima survive.',{'remaining':entries,'minimum':entries[-1][1]})

    add('linked-queue-state','Empty and singleton queue states',[
        row('New queue: no reachable nodes',[],'head = tail = None; size = 0.',chain=True),
        row('Illustrative later state: enqueue(23)',[23],'head = tail = this node; size = 1.',[0],True,False),
        row('After removing that only node',[],'Return 23; head = tail = None; size = 0.',chain=True)],
        'A nonempty tail always has next = None.',{'empty':{'head':None,'tail':None,'size':0},'singleton':{'head':23,'tail':23,'size':1},'removed':23})
    links={23:None};head=tail=23;links[tail]=41;tail=41;links[41]=None
    assert head==23 and tail==41 and links[23]==41
    add('enqueue-item','Enqueue links the old rear first',[
        row('Before enqueue(41)',[23],'head = tail = node 23; size = 1.',[0],True,False),
        row('1. old_tail.next = new node',[23,41],'head = 23; tail still = 23; new.next = None.',[1],True,False),
        row('2. tail = new; size += 1',[23,41],'head = 23; tail = 41; size = 2; return None.',[1],True,False),
        row('Empty case: enqueue(41)',[41],'head = tail = new node; size 0 → 1.',[0],True,False)],
        'Preserve the old tail until its next link is assigned.',{'head':head,'tail':tail,'links':links,'size':2})
    q=deque([23,41]);before=list(q);v=q[0];assert list(q)==before and v==23
    add('peek-queue','Peek keeps both queue endpoints',[
        row('Before peek()',before,'head = 23; tail = 41; size = 2.',[0],True,False),
        row('Returned value',[v],'Read head.value; do not dequeue.',[0],False,False),
        row('After peek(): same nodes and links',q,'head = 23; tail = 41; size = 2.',[0],True,False)],
        'Empty queue: raise IndexError without mutation.',{'before':before,'after':list(q),'returned':v,'unchanged':list(q)==before})
    d=deque();removed=[];rows=[]
    for op,val in [('right',23),('left',11),('right',41),('take_right',None),('take_left',None)]:
        if op=='right':d.append(val)
        elif op=='left':d.appendleft(val)
        else:removed.append(d.pop() if op=='take_right' else d.popleft())
        rows.append(row(f'{op}'+(f'({val})' if val else ''),d,f'Left → right; removed so far: {removed}.'))
    assert removed==[41,11] and list(d)==[23]
    add('deque-basics','A deque changes either end',rows,'Return ([41, 11], [23]); empty takes do nothing.',{'removed':removed,'remaining':list(d)})
    data=[31,None,None,17,23];head=3;size=3;logical=[data[(head+j)%5] for j in range(size)]
    assert logical==[17,23,31] and (head+size)%5==1
    add('ring-buffer-state','Physical slots versus FIFO order',[
        row('New RingQueue(5)',[None]*5,'head = 0; size = 0; every slot is unused.'),
        row('Illustrative wrapped state',data,'head = 3; size = 3; capacity = 5.',[3,4,0]),
        row('Logical order: offsets 0, 1, 2',logical,'Physical indices 3, 4, 0; next write index 1.',[0])],
        'size determines occupancy; None may be valid data.',{'physical':data,'head':head,'size':size,'logical':logical,'next_write':1})
    data=[31,None,None,23];head=3;size=2;before=data.copy();v=data[head];data[head]=None;head=(head+1)%4;size-=1
    rows=[row('Before dequeue(): capacity 4',before,'head = 3; size = 2; logical order [23, 31].',[3,0]),row('Return 23; clear slot 3',data,'head = 0; size = 1; no values shift.',[0])]
    v2=data[head];data[head]=None;head=(head+1)%4;size-=1
    assert v==23 and v2==31 and head==1 and size==0
    rows.append(row('Return 31; remove the final item',data,'head = 1; size = 0 (do not reset head).'))
    add('ring-dequeue','Dequeue advances through the wrap',rows,'An empty dequeue raises IndexError unchanged.',{'returned':[v,v2],'final_data':data,'head':head,'size':size})
    q=deque([('cut',2),('dry',1)]);log=[];rows=[row('Before: (job, units remaining)',['cut:2','dry:1'],'Front on left; one unit per turn.',[0])]
    while q:
        name,n=q.popleft();log.append(name)
        if n>1:q.append((name,n-1))
        rows.append(row('Serve '+name,[f'{k}:{v}' for k,v in q],f'Service log: {", ".join(log)}.'))
    assert log==['cut','dry','cut']
    add('round-robin','Unfinished work rejoins the rear',rows,'Zero-unit jobs take no turns; input stays unchanged.',{'log':log,'input':[['cut',2],['dry',1]]})

    h=0;rows=[row('Start: hash key AZ with capacity 7',[h],'Accumulator h = 0; no bucket is written.',indices=False)]
    for c in 'AZ':
        prev=h;h=(31*h+ord(c))%7
        rows.append(row(f'Read {c}: ord({c}) = {ord(c)}',[h],f'({prev} × 31 + {ord(c)}) % 7 = {h}',[0],indices=False))
    assert h==hash_index('AZ',7)
    add('hash-to-bucket','Roll each character into a bucket',rows,'Return bucket index 5; empty key maps to 0.',{'key':'AZ','capacity':7,'bucket':h})
    a=[[] for _ in range(4)];b=[[] for _ in range(4)];assert len({id(x) for x in a+b})==8
    add('table-state','Each bucket is a distinct list',[
        row('New HashTable(4): buckets',['[]']*4,'size = 0; capacity = 4; no stored pairs.'),
        row('Illustrative later state: put(A, 7)',['[]','A:7','[]','[]'],'A hashes to 1; size = 1.',[1]),
        row('A second new table remains empty',['[]']*4,'Its bucket 1 is a different list object.')],
        'size counts keys, not allocated or occupied buckets.',{'independent_bucket_objects':8,'initial_size':0,'bucket_A':hash_index('A',4)})
    assert hash_index('A',4)==hash_index('E',4)==hash_index('I',4)==1
    bucket=[('A',7)];rows=[row('Before: bucket 1 of 4',['A:7'],'size = 1; pairs retain keys as well as values.',indices=False)]
    bucket.append(('E',9));rows.append(row('put(E, 9): collision, new key',[f'{k}:{v}' for k,v in bucket],'A != E; append E; size 1 → 2.',[1],indices=False))
    bucket[0]=('A',12);rows.append(row('put(A, 12): equal key, replace pair',[f'{k}:{v}' for k,v in bucket],'size stays 2; both calls return None.',[0],indices=False))
    assert len(bucket)==2 and dict(bucket)=={'A':12,'E':9}
    add('insert-or-update','Collision is not replacement',rows,'Teaching hash: A and E both map to bucket 1 of 4.',{'bucket':bucket,'size':len(bucket),'capacity':4})
    bucket=[('A',7),('E',9)];before=bucket.copy();v=next(v for k,v in bucket if k=='E');assert v==9 and bucket==before
    add('lookup-key','Lookup compares keys, not hashes',[
        row('get(E): bucket 1 of 4',['A:7','E:9'],'A != E: skip first pair; E == E: match.',[1],indices=False),
        row('Returned value',[v],'Do not return the first value, 7.',[0],indices=False),
        row('After: bucket 1 is unchanged',['A:7','E:9'],'size stays 2; pair order and values stay intact.',indices=False)],
        'get(I): same bucket, no equal key → KeyError.',{'before':before,'after':bucket,'returned':v})
    bucket=[('A',7),('E',9),('I',12)];before=bucket.copy();bucket.pop(1);assert bucket==[('A',7),('I',12)]
    add('delete-key','Delete one pair, keep its neighbors',[
        row('Before delete(E): bucket 1 of 4',[f'{k}:{v}' for k,v in before],'size = 3; find E at bucket position 1.',[1]),
        row('After: pop bucket position 1',[f'{k}:{v}' for k,v in bucket],'I shifts left; size = 2; return True.',[1]),
        row('delete(E) again: unchanged',[f'{k}:{v}' for k,v in bucket],'No equal key remains; return False.')],
        'All three keys hash to 1; deletion checks equality.',{'before':before,'after':bucket,'returns':[True,False]})
    add('load-factor','Load counts keys, not busy buckets',[
        row('Before: n = 2 keys, m = 4 buckets',['[]','A:7 E:9','[]','[]'],'Only bucket 1 is occupied; load = 2 / 4 = 0.5.',[1]),
        row('Insert I:12 into the same bucket',['A:7','E:9','I:12'],'n = 3; m = 4; load = 3 / 4 = 0.75.',indices=False),
        row('Update E:9 to E:20',['A:7','E:20','I:12'],'n stays 3; load remains 0.75.',[1],indices=False)],
        'Reading load_factor() never triggers a resize.',{'before':2/4,'after_insert':3/4,'after_update':3/4})
    entries=[('A',7),('E',9),('I',12)];old=[hash_index(k,4) for k,v in entries];new=[hash_index(k,8) for k,v in entries];assert old==[1,1,1] and new==[1,5,1]
    add('rehash-table','Rehash the key, not its old index',[
        row('Before: capacity 4; bucket 1',['A:7','E:9','I:12'],'size = 3; all other buckets are empty.',indices=False),
        row('After rehash(8): new bucket 1',['A:7','I:12'],'65 % 8 = 1; 73 % 8 = 1.',indices=False),
        row('After rehash(8): new bucket 5',['E:9'],'69 % 8 = 5; other new buckets are empty.',[0],indices=False),
        row('Original key order: A, E, I',new,'New bucket indices; size stays 3; values move too.',indices=False)],
        'The explicit rebuild keeps every key/value pair.',{'keys':[k for k,v in entries],'old_buckets':old,'new_buckets':new,'size':3})
    slots=['G:8','K:6',None,'C:4'];assert all(hash_index(k,4)==3 for k in ['C','G','K'])
    add('linear-probing','A lookup follows the wrapped probe',[
        row('Before get(K): capacity 4',slots,'Home = ord(K) % 4 = 3.',[3]),
        row('Probe 3 → 0 → 1',slots,'C != K; G != K; K matches → return 6.',[1]),
        row('After: slots remain unchanged',slots,'Missing O probes 3, 0, 1, 2; None ends search.')],
        'Skip deletion markers; never exceed capacity probes.',{'slots':slots,'home':3,'probes':[3,0,1],'returned':6,'missing_probes':[3,0,1,2]})

    a=[18,7,25,7];target=7;idx=next((i for i,v in enumerate(a) if v==target),-1);assert idx==1
    add('linear-search','Return the first matching index',[
        row('Before: search target 7',a,'Unsorted input; scan from index 0.',[0]),
        row('Index 0: 18 != 7; index 1: 7 == 7',a,'Return index 1; index 3 need not be read.',[1]),
        row('After: the original list is unchanged',a,'Missing target 99 examines all 4; returns -1.')],
        'An empty input returns -1 without indexing.',{'values':a,'target':target,'visited':[0,1],'result':idx})
    def search_rows(a,target,lo,hi):
        rows=[];events=[]
        while lo<hi:
            mid=lo+(hi-lo)//2;v=a[mid];events.append([lo,hi,mid,v])
            if v==target:note=f'a[{mid}] = {target}; return original index {mid}.'
            elif v<target:note=f'{v} < {target}: lo becomes {mid+1}; hi stays {hi}.'
            else:note=f'{v} > {target}: hi becomes {mid}; lo stays {lo}.'
            rows.append(row(f'Candidates [{lo}, {hi}); mid = {mid}',a,note,[mid]))
            if v==target:return rows,events,mid
            if v<target:lo=mid+1
            else:hi=mid
        rows.append(row(f'Stop: empty interval [{lo}, {hi})',a,'Return -1; input remains unchanged.'))
        return rows,events,-1
    a=[4,9,16,23,31,42];rows,events,result=search_rows(a,31,0,len(a));assert result==4
    add('binary-search-loop','A half-open interval shrinks',rows,'lo is included; hi is excluded; no slicing.',{'values':a,'target':31,'events':events,'result':result})
    a=[4,9,9,23,31];rows,events,result=search_rows(a,31,1,4);assert result==-1 and all(1<=e[2]<4 for e in events)
    add('binary-search-boundaries','The excluded endpoint is not searched',rows,'Initial [1, 4) excludes index 4, even though it is 31.',{'values':a,'target':31,'initial_bounds':[1,4],'events':events,'result':result})
    a=[4,9,9,9,23];lo=0;hi=len(a);rows=[];events=[]
    while lo<hi:
        mid=(lo+hi)//2;events.append([lo,hi,mid]);note=f'{a[mid]} <= 9: lo = {mid+1}.' if a[mid]<=9 else f'{a[mid]} > 9: hi = {mid}.'
        rows.append(row(f'Bounds [{lo}, {hi}); mid = {mid}',a,note,[mid]))
        if a[mid]<=9:lo=mid+1
        else:hi=mid
    assert lo==bisect.bisect_right(a,9)==4
    rows.append(row('Meet at 4: upper_bound returns 4',a,'First value > 9; equal run is [1, 4).',[4]))
    add('upper-bound','Equality sends the search right',rows,'If no value is greater, return len(values).',{'events':events,'upper_bound':lo,'lower_bound':bisect.bisect_left(a,9)})
    a=[4,9,9,23];pos=bisect.bisect_right(a,9);rows=[row('Before: insert another 9',a,'Upper bound is 3: after both existing 9s.')];a.append(9)
    rows.append(row('Append a temporary extra slot',a,'Copy backward: index 3 → index 4.',[4]))
    for j in range(len(a)-1,pos,-1):a[j]=a[j-1]
    rows.append(row('After shifting 23 right',a,'Index 3 can now be overwritten.',[4]));a[pos]=9
    rows.append(row('Write 9 at index 3',a,'Return 3; mutate the same list object.',[3]));assert a==[4,9,9,9,23]
    add('sorted-insertion','Locate quickly; shift the suffix',rows,'Backward copying prevents overwriting a source.',{'position':pos,'after':a})

    a=[11,7,19];before=a.copy();a[0],a[1]=a[1],a[0];assert a==[7,11,19]
    add('swap-adjacent','Swap only an inverted adjacent pair',[
        row('Before: compare indices 0 and 1',before,'11 > 7: this adjacent pair is inverted.',[0,1]),
        row('After: exchange the two values',a,'Index 2 stays 19; the multiset is unchanged.',[0,1]),
        row('Compare indices 1 and 2',a,'11 <= 19: no swap; keep this state.')],
        'Illustrative ascending adjacent-swap rule.',{'before':before,'after':a})
    a=[18,7,13,4];rows=[row('Before one left-to-right pass',a,'Compare adjacent pairs from index 0.')];events=[]
    for j in range(len(a)-1):
        old=a.copy()
        if a[j]>a[j+1]:a[j],a[j+1]=a[j+1],a[j]
        events.append(a.copy());rows.append(row(f'After comparing indices {j} and {j+1}',a,f'{old[j]} > {old[j+1]}: swap.',[j,j+1]))
    assert a==[7,13,4,18]
    add('bubble-pass','One pass moves the maximum right',rows,'18 is final; the prefix is not sorted yet.',{'states':events,'after':a})
    a=[18,7,13,4];rows=[row('Before: unsorted input',a,'Ascending bubble sort; final suffix grows.')];events=[]
    for end in range(len(a)-1,0,-1):
        for j in range(end):
            if a[j]>a[j+1]:a[j],a[j+1]=a[j+1],a[j]
        events.append(a.copy());rows.append(row(f'Pass ends at index {end}',a,f'Indices {end} through 3 are final.',range(end,4)))
    assert a==[4,7,13,18]
    add('bubble-sort','Bubble sort freezes a suffix',rows,'Never compare inside the already final suffix.',{'passes':events,'result':a})
    a=[18,7,13,4];minimum=0;rows=[row('Scan suffix [0, 4): candidate index 0',a,'Candidate minimum = 18.',[0])]
    for j in range(1,len(a)):
        if a[j]<a[minimum]:minimum=j
        rows.append(row(f'After reading index {j}',a,f'Candidate index {minimum}; value {a[minimum]}.',[minimum]))
    assert minimum==3
    add('select-minimum','Remember the minimum index',rows,'The scan reads values; it does not swap yet.',{'values':a,'minimum_index':minimum,'value':a[minimum]})
    a=[18,7,13,4];rows=[row('Before: unsorted input',a,'Select a minimum for each prefix boundary.')];events=[]
    for i in range(len(a)-1):
        j=min(range(i,len(a)),key=a.__getitem__);a[i],a[j]=a[j],a[i];events.append(a.copy());rows.append(row(f'i = {i}: swap positions {i} and {j}',a,f'Prefix [0, {i+1}) is now final.',range(i+1)))
    assert a==[4,7,13,18]
    add('selection-sort','Selection sort grows a final prefix',rows,'Even a self-swap leaves the invariant intact.',{'passes':events,'result':a})
    a=[4,13,18,7];key=a[3];rows=[row('Before: sorted prefix [0, 3)',a,'Save key = 7 outside the array.',[3])];j=2;events=[]
    while j>=0 and a[j]>key:
        a[j+1]=a[j];events.append(a.copy());rows.append(row(f'Shift index {j} → {j+1}',a,'Saved key remains 7; duplicate is temporary.',[j+1]));j-=1
    a[j+1]=key;rows.append(row('Write saved key at index 1',a,'The full prefix [0, 4) is sorted.',[1]));assert a==[4,7,13,18]
    add('insertion-step','Keep the key while shifting larger items',rows,'Shift only values greater than the saved key.',{'shift_states':events,'key':key,'result':a})
    a=[18,7,13,4];rows=[row('Before: prefix [0, 1) is sorted',a,'Insert each next value into the sorted prefix.',[0])];events=[]
    for i in range(1,len(a)):
        key=a[i];j=i-1
        while j>=0 and a[j]>key:a[j+1]=a[j];j-=1
        a[j+1]=key;events.append(a.copy());rows.append(row(f'Insert saved key {key} from index {i}',a,f'Prefix [0, {i+1}) is sorted, not necessarily final.',range(i+1)))
    assert a==[4,7,13,18]
    add('insertion-sort','A sorted prefix can still shift later',rows,'A sorted prefix differs from selection’s final prefix.',{'passes':events,'result':a})
    a=[18,7,13,4];left=sorted(a[:2]);right=sorted(a[2:]);out=[];i=j=0;choices=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:out.append(left[i]);i+=1;choices.append('L')
        else:out.append(right[j]);j+=1;choices.append('R')
    out.extend(left[i:]);out.extend(right[j:]);assert out==sorted(a)
    add('merge-sort','Split, sort the halves, then merge',[
        row('Input; split between indices 1 and 2',a,'Left [18, 7]; right [13, 4].'),
        row('Singleton leaves',a,'[18] + [7] and [13] + [4]; base cases.'),
        row('Merge each pair into sorted runs',left+right,'Left [7, 18]; right [4, 13].',[0,1]),
        row('Final merge: R4, L7, R13, remaining L18',out,'Compare front values; preserve every occurrence.',range(4))],
        'Illustrative top-down merge sort with fresh output.',{'input':a,'left':left,'right':right,'choices':choices,'result':out})
    a=[18,7,13,4,13];pivot=13;less=[x for x in a if x<pivot];equal=[x for x in a if x==pivot];greater=[x for x in a if x>pivot];result=sorted(less)+equal+sorted(greater);assert result==sorted(a)
    add('quicksort','Three-way quicksort keeps equal keys',[
        row('Input: choose pivot value 13',a,'Illustrative allocating three-way variant.',[2,4]),
        row('Partition: less | equal | greater',less+equal+greater,'[7, 4] | [13, 13] | [18]',[2,3]),
        row('Recurse only on less and greater',[4,7,18],'Sort [7, 4] → [4, 7]; [18] is a base case.'),
        row('Concatenate sorted less + equal + greater',result,'Both copies of 13 remain; all values preserved.',[2,3])],
        'New lists are used; this is not in-place partitioning.',{'input':a,'pivot':pivot,'less':less,'equal':equal,'greater':greater,'result':result})

def main():
    build();assert len(PLAN)==len(SCENES)==35
    placements=[];traces=[]
    for p in PLAN:
        slug=p['lesson'].split('/')[1][3:];s=SCENES[slug];rows=s['rows'];height=110+len(rows)*112
        desc=' '.join(r['label']+': '+str(r['values'])+'. '+r['note'] for r in rows)
        f=Figure(s['title'],desc,height)
        for i,r in enumerate(rows):
            y=72+i*112;f.text(24,y,r['label'],16)
            vals=['None' if v is None else str(v) for v in r['values']]
            if not vals:f.box(40,y+20,120,40,'empty',GRAY)
            elif r['chain']:
                w=85;gap=55;f.chain(vals,y+20,x=40,w=w,gap=gap,colors={j:ORANGE for j in r['hot']})
            else:
                w=min(140,440/len(vals));x=30
                f.cells(vals,y+27,x=x,w=w,h=38,colors={j:ORANGE for j in r['hot']},indices=r['indices'])
            f.text(24,y+88,r['note'],14)
        svg=f.finish(s['caption']);canonical=OUT/p['file'];local=ROOT/p['lesson']/p['file'];local.parent.mkdir(parents=True,exist_ok=True)
        canonical.write_text(svg);local.write_text(svg)
        lesson=ROOT/p['lesson']/'lesson.md'
        placements.append({**p,'alt':desc,'caption':s['caption']+' Original illustrative example; not exercise input.','context':'Place after the conceptual operation explanation and before Your Tasks. '+('Match the existing lesson contract.' if lesson.exists() else 'Lesson prose not yet present: named illustrative variant, not an assessment contract.'),'canonical_svg':str(canonical.relative_to(ROOT)),'local_svg':str(local.relative_to(ROOT)),'canonical_editable':str((OUT/p['editable']).relative_to(ROOT)),'local_editable':str((ROOT/p['lesson']/p['editable']).relative_to(ROOT)),'lesson_contract_present':lesson.exists(),'lesson_sha256_at_generation':hashlib.sha256(lesson.read_bytes()).hexdigest() if lesson.exists() else None})
        traces.append({'lesson':p['lesson'],'file':p['file'],'assertions_passed':True,'trace':s['checks']})
    (OUT/'placements-extra-06-10.json').write_text(json.dumps(placements,indent=2)+'\n')
    (OUT/'traces-extra-06-10.json').write_text(json.dumps(traces,indent=2)+'\n')
    print(json.dumps({'canonical_svg':len(placements),'local_svg':len(placements),'asserted_scenes':len(traces),'missing_lesson_contracts':[p['lesson'] for p in placements if not p['lesson_contract_present']]},indent=2))
if __name__=='__main__':main()
