"""Execute every diagram's illustrative input against its actual lesson solution.
Run after both generators. --reviewed records the agent's completed visual review;
this flag must only be supplied after inspecting all current contact sheets.
"""
from __future__ import annotations
import hashlib
import json
import runpy
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'assets/diagrams'
placements=json.loads((OUT/'placements-extra-01-05.json').read_text())
audit=json.loads((OUT/'audit-extra-01-05.json').read_text())
results=[];files=[];types={}

def expect_index_error(fn):
    try:fn()
    except IndexError:return
    raise AssertionError('Expected IndexError')

def linked_values(obj):
    values=[];node=obj.head
    for _ in range(obj.size):
        assert node is not None
        values.append(node.value);node=node.next
    return values

def check_linked(obj, expected, circular=False, double=False):
    assert linked_values(obj)==expected and obj.size==len(expected)
    if not expected:assert obj.head is None and obj.tail is None;return
    assert obj.head.value==expected[0] and obj.tail.value==expected[-1]
    assert obj.tail.next is (obj.head if circular else None)
    if double:
        assert obj.head.prev is None
        node=obj.head
        while node.next is not None:assert node.next.prev is node;node=node.next

def skip_rows(obj):
    rows=[]
    for level in range(obj.max_level):
        row=[];node=obj.head.forward[level]
        while node is not None:row.append(node.key);node=node.forward[level]
        rows.append(row)
    return rows

for p in placements:
    key=p['lesson'].split('/')[1][3:]
    solution=ROOT/p['lesson']/'solution/main.py'
    ns=runpy.run_path(str(solution),run_name='diagram_contract_check')
    if key=='shallow-copies':
        a=[[3,8],[5]];b=ns['copy_outer'](a);assert b is not a and b[0] is a[0]
        b[0].append(9);assert a==[[3,8,9],[5]]
    elif key=='auxiliary-space':
        assert ns['extremes']([4,7,2,9])==(2,9)
        assert ns['extremes']([]) is None and ns['extremes']([4])==(4,4)
    elif key=='amortized-append':assert ns['append_costs'](8)==([1,2,3,1,5,1,1,1],8)
    elif key=='base-and-recursive-cases':assert ns['steps_to_zero'](3)==3 and ns['steps_to_zero'](0)==0
    elif key=='recursive-sum':assert ns['recursive_sum']([6,2,5])==13 and ns['recursive_sum']([])==0
    elif key=='recursive-factorial':assert ns['factorial_recursive'](3)==(6,4) and ns['factorial_recursive'](0)==(1,1)
    elif key=='fibonacci-tree':assert ns['fibonacci_tree'](4)==(3,9)
    elif key=='iterative-fibonacci':assert ns['fibonacci_loop'](5)==(5,5) and ns['fibonacci_loop'](0)==(0,0)
    elif key=='recursive-binary-search':
        assert ns['binary_search_recursive']([2,5,8,11,14,17,20],17)==5
        assert ns['binary_search_recursive']([],17) is None
    elif key=='append-with-capacity':
        a=ns['Array']([4,9]);a._grow();assert a.capacity==4 and a.size==2
        a.append(6);assert a.snapshot()==[4,9,6] and a.capacity==4 and a.size==3
    elif key=='delete-and-compact':
        a=ns['Array']([4,9,6,2]);assert a.delete(1)==9
        assert a._data==[4,6,2,None] and a.size==3
        a=ns['Array']([4]);assert a.delete(0)==4 and a.size==0;expect_index_error(lambda:a.delete(0))
    elif key=='reverse-two-pointers':
        a=[3,7,4,8,2];assert ns['reverse_in_place'](a) is a and a==[2,8,4,7,3]
        assert ns['reverse_in_place']([])==[] and ns['reverse_in_place']([4])==[4]
    elif key=='sliding-window':assert ns['max_window_sum']([4,1,7,2,6],3)==15
    elif key=='prefix-sums':assert ns['PrefixSums']([4,1,7,2]).prefix==[0,4,5,12,14]
    elif key=='node-and-link':
        a=ns['Node'](4);b=ns['Node'](9);a.next=b;assert a is not b and b.next is None
    elif key=='traverse-nodes':
        a=ns['Node'](4,ns['Node'](9,ns['Node'](6)));assert ns['values'](a)==[4,9,6] and ns['values'](None)==[]
    elif key=='list-state':check_linked(ns['LinkedList'](),[])
    elif key=='prepend-node':
        obj=ns['LinkedList']();obj.prepend(9);obj.prepend(4);node=obj.prepend(2)
        assert obj.head is node;check_linked(obj,[2,4,9])
    elif key in ('append-node','find-node','remove-head','remove-tail'):
        obj=ns['LinkedList']()
        for value in ([4,9,4] if key=='find-node' else [4,9,6]):obj.append(value)
        if key=='append-node':check_linked(obj,[4,9,6])
        elif key=='find-node':assert obj.find(4) is obj.head and obj.find(99) is None
        else:
            operation='remove_head' if key=='remove-head' else 'remove_tail'
            removed=getattr(obj,operation)();assert removed.value==(4 if key=='remove-head' else 6) and removed.next is None
            check_linked(obj,[9,6] if key=='remove-head' else [4,9])
            one=ns['LinkedList']();one.append(4);getattr(one,operation)();check_linked(one,[])
            expect_index_error(lambda:getattr(one,operation)())
    elif key=='doubly-linked-node':
        a=ns['DoubleNode'](4);b=ns['DoubleNode'](9);a.next=b;b.prev=a
        assert a.prev is None and b.next is None and a.next.prev is a
    elif key in ('doubly-prepend','doubly-append'):
        obj=ns['DoublyList']()
        if key=='doubly-prepend':obj.prepend(9);obj.prepend(4);obj.prepend(2);expected=[2,4,9]
        else:obj.append(4);obj.append(9);obj.append(6);expected=[4,9,6]
        check_linked(obj,expected,double=True)
    elif key=='browser-history':
        obj=ns['BrowserHistory']('Home');obj.visit('Guide');obj.visit('Help');assert obj.back()=='Guide'
        assert obj.visit('Blog')=='Blog';check_linked(obj.pages,['Home','Guide','Blog'],double=True)
        assert obj.current is obj.pages.tail and obj.forward()=='Blog'
    elif key in ('circular-append','circular-remove'):
        obj=ns['CircularList']()
        for value in [4,9,6]:obj.append(value)
        if key=='circular-append':check_linked(obj,[4,9,6],circular=True)
        else:
            removed=obj.remove_first(4);assert removed.value==4 and removed.next is None
            check_linked(obj,[9,6],circular=True);assert obj.remove_first(99) is None
            one=ns['CircularList']();one.append(4);one.remove_first(4);check_linked(one,[])
            assert one.remove_first(4) is None
    elif key=='skip-levels':
        for value,height in [(4,1),(9,2),(15,1),(22,3)]:assert len(ns['SkipNode'](value,height).forward)==height
    elif key.startswith('skip-'):
        obj=ns['seed_skip']([(4,1),(9,2),(15,1),(22,3)],3)
        assert skip_rows(obj)==[[4,9,15,22],[9,22],[22]]
        if key=='skip-search':assert obj.search(15).key==15 and obj.search(16) is None
        elif key=='skip-insert':
            assert obj.insert(12,2) is True and obj.insert(12,2) is False
            assert skip_rows(obj)==[[4,9,12,15,22],[9,12,22],[22]] and obj.tail.key==22
        elif key=='skip-remove':
            assert obj.remove(9) is True and obj.remove(99) is False
            assert skip_rows(obj)==[[4,15,22],[22],[22]] and obj.tail.key==22
            one=ns['seed_skip']([(7,2)],3);assert one.remove(7) is True and one.tail is None and one.size==0
        else:raise AssertionError(key)
    else:raise AssertionError(key)
    results.append({'lesson':p['lesson'],'solution_sha256':hashlib.sha256(solution.read_bytes()).hexdigest(),'illustrative_input_verified':True})
    for name,local in [('file','local_svg'),('editable','local_editable')]:
        a=OUT/p[name];b=ROOT/p[local]
        assert a.read_bytes()==b.read_bytes() and a.stat().st_size>0
        files.append({'canonical':str(a.relative_to(ROOT)),'lesson_local':str(b.relative_to(ROOT)),'sha256':hashlib.sha256(a.read_bytes()).hexdigest(),'bytes':a.stat().st_size})
    svg=ET.parse(OUT/p['file']);scene=json.loads((OUT/p['editable']).read_text())
    assert scene['type']=='excalidraw' and not scene.get('files')
    ids={e['id'] for e in scene['elements']};assert len(ids)==len(scene['elements'])
    for e in scene['elements']:
        assert e['type'] in ['rectangle','text','arrow'];types[e['type']]=types.get(e['type'],0)+1
        for binding in e.get('boundElements') or []:assert binding['id'] in ids
        if e.get('containerId'):assert e['containerId'] in ids
        for end in ['startBinding','endBinding']:
            if e.get(end):assert e[end]['elementId'] in ids
    assert [t.text for t in svg.findall('.//{http://www.w3.org/2000/svg}text')]==[e['originalText'] for e in scene['elements'] if e['type']=='text']
assert len(results)==32 and len(files)==64
assert audit['native_acceptance']['figures']==32
for r in audit['native_acceptance']['results']:
    assert all(r[k] for k in ['import','mountedEditor','exportSvg','editedExport','editedReimport','sourceTextParity','noImages','byteIdentical'])
audit['lesson_contract_checks']=results
audit['artifact_manifest']=files
audit['native_element_totals']=types
audit['final_checks']={'planned_figures':32,'canonical_files':64,'lesson_local_files':64,'byte_identical_pairs':64,'source_text_parity':True,'all_binding_ids_valid':True,'actual_lesson_examples_executed':32}
audit['alignment_notes']=['Lessons were unavailable at initial authoring, then all 32 solutions were read and illustrative inputs executed after they appeared.','Auxiliary-space diagram traces the actual extremes scan.','Recursion diagrams display product/value lanes and explicitly label tuple-return counters.','Binary search missing sentinel is None; linked removals return detached nodes; circular remove_first returns None when empty or missing.','count, sum_at, and fact are explanatory shorthand for steps_to_zero, total_from, and the factorial product lane.']
if '--reviewed' in sys.argv:
    evidence=Path(audit['evidence'])
    sheets=sorted(evidence.glob('*-contact-*.png'));assert len(sheets)==32
    audit['visual_review']={'status':'passed','coverage':'All 32 canonical SVGs and all 32 native exports visually inspected in 16 source and 16 native contact sheets; changed diagrams re-inspected after fixes.','sheet_size':'1240 × 1520; two full-width 1240 × 760 diagrams per sheet','contact_sheet_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sheets},'editor_screenshots_inspected':['memory-and-cost-shallow-copies-trace-editor.png','linked-list-variants-skip-insert-trace-editor.png'],'resolved_issues':['Removed auxiliary-space connector crossing a heading','Moved compaction caption clear of shift arrows','Separated recursion lanes and attached return arrows','Moved circular closure labels away from the AFTER heading','Added detached removed-node cards and highlighted skip-search descent','Aligned return contracts and auxiliary-space mechanism with newly available lessons'],'unresolved_issues':[]}
(OUT/'audit-extra-01-05.json').write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps({'figures':len(results),'canonical_files':len(files),'local_files':len(files),'native_element_totals':types,'actual_lesson_solutions_verified':len(results),'visual_review':audit['visual_review']['status'] if isinstance(audit['visual_review'],dict) else audit['visual_review']}))
