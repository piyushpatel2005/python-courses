#!/usr/bin/env python3
"""Audit exact owned plan coverage and build all-original/native/editor contact sheets.
Run with scratch/data-structures-reference/venv/bin/python (Pillow installed).
Pass --reviewed only after visually reviewing all generated contact sheets.
"""
from pathlib import Path
from PIL import Image, ImageDraw
import json, hashlib, sys
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'assets/diagrams'
placements=json.loads((OUT/'placements-extra-06-10.json').read_text())
plan=[p for p in json.loads((ROOT/'assets/additional-diagram-plan.json').read_text()) if 6<=int(p['lesson'][:2])<=10]
audit_path=OUT/'audit-extra-06-10.json';audit=json.loads(audit_path.read_text())
assert len(placements)==len(plan)==len(audit['diagrams'])==35
assert {p['file'] for p in placements}=={p['file'] for p in plan}=={d['file'] for d in audit['diagrams']}
assert not audit['errors'] and not audit['geometryFailures']
checks=[]
for p in placements:
    record={'file':p['file']}
    for ext in ['svg','editable']:
        a=(ROOT/p['canonical_'+ext]).read_bytes();b=(ROOT/p['local_'+ext]).read_bytes()
        assert a and a==b;record[ext+'_sha256']=hashlib.sha256(a).hexdigest()
    scene=json.loads((ROOT/p['canonical_editable']).read_text())
    assert scene['elements'] and not scene.get('files')
    assert not any(e['type']=='image' for e in scene['elements'])
    checks.append(record)
evidence=Path(audit['evidenceDirectory']);contacts=[]
for batch,start in enumerate(range(0,len(placements),5),1):
    subset=placements[start:start+5];tiles=[];editors=[]
    for p in subset:
        stem=Path(p['file']).stem
        pair=[]
        for variant in ['original','export']:
            im=Image.open(evidence/(stem+'-'+variant+'.png')).convert('RGB');im.thumbnail((400,800));pair.append(im)
        tile=Image.new('RGB',(820,max(x.height for x in pair)+48),'#e2e8f0');draw=ImageDraw.Draw(tile)
        draw.text((10,7),p['lesson'],fill='#172033');draw.text((10,25),'CANONICAL SVG (500px rendered)',fill='#172033');draw.text((420,25),'NATIVE LIBRARY EXPORT',fill='#172033')
        for i,im in enumerate(pair):tile.paste(im,(10+i*410,44))
        tiles.append(tile)
        im=Image.open(evidence/(stem+'-editor.png')).convert('RGB');im.thumbnail((500,500));t=Image.new('RGB',(500,530),'white');t.paste(im,(0,30));ImageDraw.Draw(t).text((6,6),p['lesson'],fill='black');editors.append(t)
    sheet=Image.new('RGB',(820,sum(t.height for t in tiles)),'white');y=0
    for tile in tiles:sheet.paste(tile,(0,y));y+=tile.height
    target=evidence/f'contact-original-native-{batch:02}.png';sheet.save(target);contacts.append(str(target))
    sheet=Image.new('RGB',(1500,1060),'white')
    for i,t in enumerate(editors):sheet.paste(t,((i%3)*500,(i//3)*530))
    target=evidence/f'contact-editors-{batch:02}.png';sheet.save(target);contacts.append(str(target))
audit.update(scope='All 35 ADDITIONAL diagram-plan entries for modules 06–10; initial plan untouched',exactPlanCoverage=True,artifactHashes=checks,traceEvidence='assets/diagrams/traces-extra-06-10.json',contactSheets=contacts,originalExamples=True,lessonContractAbsentAtGeneration=[p['lesson'] for p in placements if not p['lesson_contract_present']])
if '--reviewed' in sys.argv:
    audit['visualReview']='All 35 canonical renders at native 500px, all 35 actual native SVG exports, and all 35 mounted-editor screenshots inspected through 14 contact sheets. No clipped labels, text collisions, connector crossings or hidden titles found.'
else:audit['visualReview']='Contact sheets created; visual review pending.'
audit_path.write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps({'diagrams':len(placements),'artifacts':len(checks)*4,'geometry_failures':len(audit['geometryFailures']),'contacts':contacts,'visualReview':audit['visualReview']},indent=2))
