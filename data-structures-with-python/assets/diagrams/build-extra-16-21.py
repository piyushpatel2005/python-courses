"""35 original 500px operation figures; actual lesson solutions are the oracle.
No lesson or shared helper edits. Run this, then build-extra-16-21.mjs.
"""
from pathlib import Path
import importlib.util, json, hashlib, runpy, itertools
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'assets/diagrams'
SCRATCH=Path.home()/'.hermes/profiles/curriculum-dev/cache/scratch/ds-diagrams-extra-16-21'
spec=importlib.util.spec_from_file_location('figure',OUT/'build-first-half.py'); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
Figure=mod.Figure; BLUE,GREEN,ORANGE,PURPLE,GRAY=mod.BLUE,mod.GREEN,mod.ORANGE,mod.PURPLE,mod.GRAY
PLAN=[p for p in json.loads((ROOT/'assets/additional-diagram-plan.json').read_text()) if 16<=int(p['lesson'][:2])<=21]
assert len(PLAN)==35
placements=[];checks=[]
def snap(node): return {'terminal':node.terminal,'children':{k:snap(v) for k,v in node.children.items()}}
def row(f,label,values,y,active=()):
 f.text(24,y-16,label); f.cells(values,y,x=26,w=min(88,448/len(values)),colors={i:GREEN for i in active})
def lines(f,items,y=330):
 for i,t in enumerate(items):f.text(24,y+i*29,t,16)
def trie(f,y=100,terminal=False,branch=True):
 for x,s in [(25,'root'),(145,'b'),(265,'e')]: f.box(x,y,75,40,s)
 f.arrow((100,y+20),(145,y+20));f.arrow((220,y+20),(265,y+20))
 f.box(385,y,85,40,'e *',GREEN);f.arrow((340,y+20),(385,y+20))
 if branch:
  f.box(385,y+85,85,40,'t *',GREEN);f.arrow((302,y+40),(302,y+105),(385,y+105))
 if terminal:f.text(270,y-14,'*',16)
def tree(f,vals,y=100,minimum=False,layout=False):
 a,b,c=vals;leaves=[a,b,c,'∞' if minimum else 0]
 sums=[min(a,b) if minimum else a+b,c if minimum else c,(min(vals) if minimum else sum(vals))]
 positions=[(210,y,70,sums[2]),(95,y+90,85,sums[0]),(320,y+90,85,sums[1])]
 for x,yy,w,v in positions:f.box(x,yy,w,40,0 if layout else v,GREEN)
 f.arrow((227,y+40),(137,y+90));f.arrow((263,y+40),(362,y+90))
 for i,v in enumerate(leaves):
  x=25+i*120;f.box(x,y+190,85,40,v,GRAY if i==3 else BLUE)
  f.text(x+42,y+256,f'[{i},{i+1})',14,'middle')
 for px,cx in [(137,67),(137,187),(362,307),(362,427)]:f.arrow((px,y+130),(cx,y+190))
 f.text(250,y-12,'[0,4)',14,'middle')
for p in PLAN:
 path=ROOT/p['lesson']/'solution/main.py';ns=runpy.run_path(str(path));key=p['lesson'].split('/')[1];m=int(p['lesson'][:2]);trace={};caption='Queries return values; state is shown separately.'
 title=key[3:].replace('-',' ').capitalize()
 if len(title)>31:title=title.replace('without replacement','no replacement').replace('with replacement','with reuse')
 f=Figure(title,'',570)
 if m==16:
  if key.startswith('01'):
   result=[ns['read_bit'](45,i) for i in [0,1,3,6]];assert result==[1,0,1,0]
   row(f,'value = 45; bit positions 5 … 0',[1,0,1,1,0,1],100,(2,));row(f,'position 3: mask = 1 << 3',[0,0,1,0,0,0],205,(2,))
   lines(f,['45 >> 3 = 5; 5 & 1 = 1','read_bit(45, 3) returns integer 1','position 1 returns 0; position 6 returns 0','Input integer remains 45; zero reads as 0.']);trace={'results':result};assert ns['read_bit'](0,0)==0
  elif key.startswith('02'):
   results=[ns['change_bit'](45,1,a) for a in ['set','clear','toggle']];assert results==[47,45,47]
   row(f,'Before: value 45; position 1 mask 000010',list('101101'),100,(4,))
   for y,a,v in zip([205,305,405],['set: OR','clear: AND NOT','toggle: XOR'],results):row(f,f'{a} → return {v}',list(f'{v:06b}'),y,(4,))
   caption='Independent calls on 45; no integer mutation.';trace={'returns':results};assert ns['change_bit'](47,1,'toggle')==45
  elif key.startswith('03'):
   v=45;states=[v]
   while v:v&=v-1;states.append(v)
   for i,v in enumerate(states):row(f,f'After {i} clears: value = {v}',list(f'{v:06b}'),90+i*84)
   assert ns['count_bits'](45)==4 and ns['count_bits'](0)==0
   caption='Return 4; input 45 unchanged. Zero returns 0.';trace={'states':states,'return':4}
  elif key.startswith('04'):
   for i,v in enumerate([16,20,0]):
    y=100+i*125;row(f,f'n = {v}; n & (n − 1) = {v&(v-1)}',list(f'{v:05b}'),y);f.text(28,y+72,f'Return {ns["is_power_of_two"](v)}',16)
   assert [ns['is_power_of_two'](v) for v in [16,20,0,-8,1]]==[True,False,False,False,True]
   caption='The positive guard rejects 0 and negatives.';trace={'inputs':[16,20,0,-8,1],'returns':[True,False,False,False,True]}
  elif key.startswith('06'):
   a=[3,7,7];b=[7,11];r=ns['compare_groups'](a,b);assert r==dict(either={3,7,11},both={7},left_only={3},exclusive={3,11})
   row(f,'Left input: duplicates collapse',[3,7,7],95);row(f,'Right input',[7,11],195)
   lines(f,['either: {3, 7, 11}     both: {7}','left_only: {3}     exclusive: {3, 11}','Return a dict of sets; inputs unchanged.','Empty vs empty: all four sets are empty.'],310)
   assert all(not s for s in ns['compare_groups']([],[]).values());trace={k:sorted(v) for k,v in r.items()}
  else:
   results=[ns['allows_all'](3,r) for r in [2,6,0]];assert results==[True,False,True]
   row(f,'Held = VIEW | EDIT = 3 (011)',list('011'),95);row(f,'Request EDIT | EXPORT = 6 (110)',list('110'),195);row(f,'Intersection = 2 (010), not 6',list('010'),295)
   lines(f,['Return False: EXPORT is missing.','Request EDIT alone → True; request 0 → True.','No flags change; all requested bits must exist.'],400);trace={'held':3,'requests':[2,6,0],'returns':results}
 elif m==17:
  if key.startswith('01'):
   a,b=ns['TrieNode'](),ns['TrieNode']();a.children['b']=ns['TrieNode']();assert b.children=={} and not a.terminal
   f.box(35,110,150,45,'node A');f.box(300,110,150,45,'node B');f.box(35,230,150,45,'child b');f.arrow((110,155),(110,230));lines(f,['A.children = {"b": child}; terminal = False','B.children = {}; terminal = False','Each node owns a distinct child dictionary.','A fresh node does not mark a complete word.'],350);trace={'A':snap(a),'B':snap(b)}
  else:
   t=ns['Trie']();t.insert('bee');before=snap(t.root)
   if key.startswith('02'):
    ret=t.insert('bet');assert ret is None;assert t.root.children['b'].children['e'].children['t'].terminal
    f.text(24,70,'Before: bee is the only word');trie(f,100,branch=False);f.text(24,220,'insert("bet"): reuse b → e; add t');trie(f,250)
    lines(f,['Return None; * marks a terminal node.','insert("") marks root; duplicate is idempotent.'],450);t.insert('');assert t.root.terminal;trace={'before':before,'after':snap(t.root),'return':ret}
   elif key.startswith('03') or key.startswith('04'):
    trie(f,100,branch=False);fn=t.contains if key.startswith('03') else t.starts_with
    qs=['be','bee','bo',''];r=[fn(x) for x in qs];assert r==([False,True,False,False] if key.startswith('03') else [True,True,False,True]);assert snap(t.root)==before
    lines(f,[f'{fn.__name__}("{q}") → {v}' for q,v in zip(qs,r)],240)
    f.text(24,400,'be has a path but is not terminal.',16);f.text(24,440,'State unchanged; * means complete word.',16);trace={'queries':qs,'returns':r,'unchanged':True}
   else:
    t.insert('bet');t.insert('be');t.insert('bee');trie(f,100,terminal=True)
    if key.startswith('05'):
     r=t.collect('be');assert r==['be','bee','bet'];assert t.collect('bo')==[]
     lines(f,['collect("be"): visit terminal be first','Then sorted child e; then sorted child t',"Return ['be', 'bee', 'bet']",'collect("bo") → []; collect("") → all words','No trie links or terminal flags change.'],300);trace={'return':r,'missing':[]}
    elif key.startswith('07'):
     r=t.count_prefix('be');assert r==3 and t.count_prefix('bo')==0
     lines(f,['count_prefix("be"): count terminal nodes','be: +1; bee: +1; bet: +1 → return 3','Duplicate insert("bee") adds no word.','Missing prefix → 0; empty prefix → 3','State unchanged; root is not terminal.'],300);trace={'count':r,'empty':t.count_prefix('')}
    else:
     r=t.suggest('be',2);assert r==(3,['be','bee']);assert t.suggest('be',0)==(3,[])
     ret=t.delete('bee');assert ret is True and t.collect('be')==['be','bet'];assert not t.delete('bee')
     lines(f,['suggest("be", 2) → (3, ["be", "bee"])','limit 0 → (3, []); total is not truncated.','delete("bee") → True; prune final e only.','After: be* → t*; prefix be stays terminal.','Delete again → False; state unchanged.'],300);trace={'suggest':r,'delete':ret,'after':snap(t.root)}
  caption='Edges are characters; * marks a stored whole word.'
 elif m==18:
  if key.startswith('01'):
   r=[ns['lowbit'](i) for i in [12,8,0]];assert r==[4,8,0]
   row(f,'index 12 = 01100',list('01100'),95,(2,));row(f,'lowbit(12) = 4 = 00100',list('00100'),195,(2,))
   f.chain([12,8,0],315,x=35,w=90,gap=65);lines(f,['Prefix walk: subtract lowbit at each step.','Blocks: [8,12) then [0,8); stop at 0.','lowbit(0) = 0; never update from index 0.'],415);trace={'returns':r}
  elif key.startswith('02'):
   t=ns['Fenwick'](4);assert t.tree==[0]*5
   row(f,'Fenwick(4): internal indices 0 … 4',t.tree,110);lines(f,['n = 4; tree has n + 1 cells.','tree[0] is unused; data positions are 0 … 3.','tree[1]: [0,1)     tree[2]: [0,2)','tree[3]: [2,3)     tree[4]: [0,4)','Fenwick(0): n = 0; tree = [0]'],240);assert ns['Fenwick'](0).tree==[0];trace={'tree':t.tree,'n':4}
  elif key.startswith('03'):
   t=ns['Fenwick'](4);before=t.tree.copy();ret=t.add(2,7);assert t.tree==[0,0,0,7,7] and ret is None
   row(f,'Before: internal indices 0 … 4',before,100);f.chain([3,4,8],225,x=35,w=90,gap=65);f.text(24,300,'position 2 → index 3 → 4 → 8 (stop)',16);row(f,'After: add 7 at visited cells',t.tree,365,(3,4));f.text(24,465,'Return None; valid position: 0 ≤ p < 4.',16);trace={'before':before,'after':t.tree,'return':ret}
  elif key.startswith('05'):
   t=ns['Fenwick'](4)
   for i,v in enumerate([6,-3,8,2]):t.add(i,v)
   before=t.tree.copy();r=t.range_sum(1,3);assert r==5 and t.range_sum(2,2)==0 and t.tree==before
   row(f,'Values: select [1,3); exclude index 3',[6,-3,8,2],100,(1,2));row(f,'tree indices 0 … 4',t.tree,215)
   lines(f,['prefix(3): tree[3] + tree[2] = 8 + 3 = 11','prefix(1): tree[1] = 6','Return 11 − 6 = 5; state unchanged.','[2,2) → 0; [0,4) → 13; [0,0) → 0'],340);trace={'return':r,'tree':t.tree}
  elif key.startswith('06'):
   t=ns['Fenwick'].from_values([6,-3,8,2]);assert t.tree==[0,6,3,8,13]
   row(f,'Input data [6, −3, 8, 2]',[6,-3,8,2],95);row(f,'After repeated add: tree indices 0 … 4',t.tree,200)
   lines(f,['add(0,6): cells 1,2,4 gain 6','add(1,−3): cells 2,4 lose 3','add(2,8): cells 3,4 gain 8','add(3,2): cell 4 gains 2','Return Fenwick object; empty → tree [0]'],315);assert ns['Fenwick'].from_values([]).tree==[0];trace={'tree':t.tree,'n':t.n}
  else:
   minimum=key.startswith('11');t=ns['MinTree' if minimum else 'SegmentTree']([6,-3,8]);layout=key.startswith('07')
   if not layout:t.build()
   if key.startswith('10'):
    before=t.tree.copy();ret=t.update(1,5);assert ret is None and t.tree==[0,19,11,8,6,5,8,0]
    tree(f,[6,5,8],100);lines(f,['Before: leaf 5 = −3; node 2 = 3; root = 11','update(1,5): leaf 5 → 5; node 2 → 11','root → 19; return None (replace, not add).','query(1,3) → 13; query(2,2) → 0'],405);trace={'before':before,'after':t.tree,'return':ret};assert t.query(1,3)==13
   elif minimum:
    tree(f,[6,-3,8],100,minimum=True);assert t.query(1,3)==-3 and t.query(2,2)==float('inf')
    lines(f,['query(1,3): leaves 5 and 6 → min(−3,8)','Return −3; [2,2) → infinity (identity).','Padding leaf 7 is infinity, not zero.','Queries leave tree unchanged.'],405);trace={'tree':t.tree,'query':-3,'empty':'infinity'}
   else:
    tree(f,[6,-3,8],100,layout=layout)
    if layout:
     assert t.tree==[0,0,0,0,6,-3,8,0];lines(f,['n = 3, size = 4; leaves start at index 4.','Leaves 4 … 7: 6, −3, 8, 0 (padding).','Internal values remain 0 until build().','Empty input: size 1; tree = [0,0].'],405)
    else:
     assert t.tree==[0,11,3,8,6,-3,8,0];lines(f,['Before build: internal nodes are all 0.','Build 3 = 8 + 0; then 2 = 6 + (−3).','Build 1 = 3 + 8 = 11; return None.','Empty build: root 0; padding stays 0.'],405)
    trace={'tree':t.tree,'n':t.n,'size':t.size}
  caption='All data intervals are half-open: [left,right).'
 elif m==19:
  D=ns['DisjointSet']
  if key.startswith('01'):
   t=D(4);row(f,'parent: each item is its own root',t.parent,110);row(f,'size: valid at roots',t.size,240);assert t.parent==[0,1,2,3] and t.size==[1]*4;lines(f,['Four singleton components; no links shared.','DSU(0): parent = []; size = [].','IDs outside [0,4) are invalid.'],380);trace={'parent':t.parent,'size':t.size}
  elif key.startswith('02'):
   t=D(4);t.parent=[0,2,3,3];before=t.parent.copy();r=t.find(1);assert r==3 and t.parent==before
   row(f,'parent indices 0 … 3',before,100);f.chain([1,2,3],245,x=35,w=90,gap=65);lines(f,['find(1): 1 → 2 → 3; parent[3] = 3','Return root ID 3, not size or component.','This find does not compress: array unchanged.','find(0) → 0 (singleton root).'],365);trace={'parent':before,'return':r,'unchanged':True}
  elif key.startswith('03'):
   t=D(4);before=t.parent.copy();ret=t.union(1,3);assert ret and t.parent==[0,3,2,3];again=t.union(1,3);assert not again
   row(f,'Before parent',before,95);row(f,'After union(1,3): root 1 links to root 3',t.parent,215,(1,));row(f,'size[3] becomes 2; others are unchanged',t.size,335,(3,));lines(f,['Return True; repeated union → False.','Only root sizes are authoritative.'],445);trace={'parent':t.parent,'size':t.size,'returns':[ret,again]}
  elif key.startswith('05'):
   t=D(5);t.parent=[1,2,2,3,3];t.size=[1,2,3,2,1];before=t.parent.copy();ret=t.union_by_size(0,4);assert ret and t.parent==[2,2,2,2,3] and t.size[2]==5
   row(f,'Before parent; root sizes: 2 → 3, 3 → 2',before,95);row(f,'After compression and linking smaller root',t.parent,240,(0,1,3));lines(f,['find_compressed(0): 0 → 1 → 2','Rewrite parent[0] = 2 (1 already points to 2).','Root 3 (size 2) links to root 2 (size 3).','Return True; size[2] = 5; 4 still points to 3.'],365);trace={'before':before,'after':t.parent,'size':t.size}
  elif key.startswith('07'):
   edges=[(1,3),(3,2),(2,1),(0,4)];r=ns['first_redundant'](5,edges);assert r==(2,1)
   f.chain([1,3,2],110,x=35,w=90,gap=65);f.arrow((390,152),(390,220),(80,220),(80,152));f.text(170,248,'closing edge (2,1)',16)
   lines(f,['(1,3): merge → True','(3,2): merge → True','(2,1): same root → False; stop here','Return edge (2,1); (0,4) is not processed.','No redundant edge / empty edges → None'],310);trace={'edges':edges,'return':r};assert ns['first_redundant'](0,[]) is None
  else:
   edges=[(0,2,7),(2,1,3),(0,1,5),(3,4,-2)];r=ns['kruskal_forest'](5,edges);assert r==([(3,4,-2),(2,1,3),(0,1,5)],6)
   f.chain([3,4],100,x=60,w=90,gap=150);f.text(245,92,'−2',16,'middle');f.chain([2,1,0],220,x=35,w=90,gap=65);f.text(157,210,'3',16);f.text(312,210,'5',16)
   lines(f,['Sorted weights: −2, 3, 5, 7','Accept −2, 3, 5; reject 7 (same root).','Return (chosen_edges, 6), not a tree object.','Two components remain: {3,4}, {0,1,2}.','Empty graph → ([], 0).'],335);assert ns['kruskal_forest'](0,[])==([],0);trace={'edges':edges,'return':r}
  caption='Arrowheads show reading order; edges are undirected.' if key.startswith(('07','08')) else 'Parent links encode components, not original edges.'
 else:
  if key.startswith('01'):
   r=ns['cartesian_product'](['K','M'],[4,9]);assert r==[('K',4),('K',9),('M',4),('M',9)]
   for i,a in enumerate(['K','M']):
    f.text(35,150+i*100,a,20)
    for j,b in enumerate([4,9]):f.box(105+j*180,115+i*100,145,55,str((a,b)))
   lines(f,['Left outer loop: finish K before M.','Return list of four ordered tuples.','Either factor empty → []; inputs unchanged.'],365);assert ns['cartesian_product']([],[])==[];trace={'return':r}
  elif key.startswith('02') or key.startswith('03'):
   fun=ns['power_set' if key.startswith('02') else 'power_set_bits'];r=fun(['K','M']);assert r==[(),('K',),('M',),('K','M')]
   if key.startswith('02'):
    row(f,'Start result',["()"],100);row(f,'Add K: old + copies with K',["()","('K',)"],210);row(f,'Add M: append copies of previous result',["('M',)","('K','M')"],320);lines(f,['Final order: (), (K,), (M,), (K,M)','Snapshot additions before extending result.'],435)
   else:
    for i,s in enumerate(r):f.box(35,95+i*85,100,45,f'{i:02b}',BLUE);f.box(230,95+i*85,230,45,str(s),GREEN);f.arrow((135,117+i*85),(230,117+i*85))
    f.text(24,470,'bit 0 chooses K; bit 1 chooses M.',16)
   assert fun([])==[()];caption='Empty input returns [()], not []. Inputs unchanged.';trace={'return':r}
  else:
   names={'04':'combinations','05':'combinations_repeated','06':'permutations','07':'words'};fun=ns[names[key[:2]]];items=['K','M','P'] if key.startswith('04') else ['K','M'];r=fun(items,2)
   expected=list(itertools.combinations(items,2)) if key.startswith('04') else list(itertools.combinations_with_replacement(items,2)) if key.startswith('05') else list(itertools.permutations(items,2)) if key.startswith('06') else list(itertools.product(items,repeat=2));assert r==expected
   f.box(190,70,120,40,'path = []');f.box(65,175,130,40,"['K']");f.box(310,175,130,40,"['M']");f.arrow((220,110),(130,175));f.arrow((280,110),(375,175))
   if key.startswith('04'):
    leaves=["('K','M')","('K','P')","('M','P')"];rules=['Choose index i; recurse with start = i + 1.','K branch: M then P; M branch: P only.','P-only branch pruned: too few choices.']
   elif key.startswith('05'):
    leaves=["('K','K')","('K','M')","('M','M')"];rules=['Choose index i; recurse with start = i.','K may repeat; after M cannot go back to K.','No (M,K): combinations ignore order.']
   elif key.startswith('06'):
    leaves=["('K','M')","('M','K')"];rules=['Mark chosen index used; skip it below.','After recording, pop path; clear used flag.','Order matters; no (K,K) or (M,M).']
   else:
    leaves=["('K','K')","('K','M')","('M','K')","('M','M')"];rules=['Every level can choose K or M again.','Record tuple(path) at length 2, then return.','Pop on unwind; both order and reuse matter.']
   for i,s in enumerate(leaves):
    x=20+i*(460/len(leaves));w=450/len(leaves)-5
    f.box(x,270,w,45,s,GREEN,14 if len(leaves)==4 else 16)
    parent=130 if (i<2 if len(leaves)!=2 else i==0) else 375
    f.arrow((parent,215),(x+w/2,270))
   lines(f,rules+['Return list of tuples above; inputs unchanged.','r = 0 → [()]; empty options, r > 0 → [].'],360)
   assert fun([],0)==[()] and fun([],2)==[];trace={'items':items,'r':2,'return':r,'zero':[()]}
 desc=' '.join(__import__('html').unescape(__import__('re').sub('<[^>]+>','',x)) for x in f.parts if x.startswith('<text'))
 f.desc=desc
 svg=f.finish(caption);(OUT/p['file']).write_text(svg)
 local=ROOT/p['lesson'];assert (local/'lesson.md').is_file();(local/p['file']).write_text(svg)
 placements.append({**p,'alt':desc,'caption':caption,'context':'After the operation contract, before the atomic exercise; independent worked data.','canonical_svg':'assets/diagrams/'+p['file'],'canonical_editable':'assets/diagrams/'+p['editable'],'local_svg':str((local/p['file']).relative_to(ROOT)),'local_editable':str((local/p['editable']).relative_to(ROOT))})
 checks.append({'lesson':p['lesson'],'solution_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'actual_solution_executed':True,'trace':trace})
SCRATCH.mkdir(parents=True,exist_ok=True)
(OUT/'placements-extra-16-21.json').write_text(json.dumps(placements,indent=2)+'\n')
(SCRATCH/'solution-traces.json').write_text(json.dumps(checks,indent=2,allow_nan=True).replace('Infinity','"infinity"')+'\n')
print(json.dumps({'count':len(placements),'solution_checks':len(checks),'module21_plan_entries':sum(x['lesson'].startswith('21-') for x in PLAN),'evidence':str(SCRATCH)}))
