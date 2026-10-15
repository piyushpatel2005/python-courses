"""Create full-reading-width review sheets and verify final hashes/copies."""
from pathlib import Path
import json, hashlib
from PIL import Image
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'assets/diagrams'
E=Path.home()/'.hermes/profiles/curriculum-dev/cache/scratch/ds-diagrams-extra-16-21/evidence'
p=json.loads((OUT/'placements-extra-16-21.json').read_text())
a=json.loads((OUT/'audit-extra-16-21.json').read_text())
assert len(p)==len(a['diagrams'])==35 and not a['geometryFailures'] and not a['errors']
for item in p:
 for kind in ['svg','editable']:
  local=ROOT/item['local_'+kind]
  assert local.parent==ROOT/item['lesson'],f'Not lesson-adjacent: {local}'
  assert (local.parent/'lesson.md').is_file()
  assert not (local.parent/'assets'/local.name).exists(),f'Misplaced duplicate: {local.name}'
  assert (ROOT/item['canonical_'+kind]).read_bytes()==local.read_bytes()
for c in a['solutionChecks']:
 path=ROOT/c['lesson']/'solution/main.py'
 assert hashlib.sha256(path.read_bytes()).hexdigest()==c['solution_sha256'],f'Solution changed: {path}'
for kind,suffix in [('canonical','original'),('native','export')]:
 for start in range(0,len(p),4):
  sheet=Image.new('RGB',(1000,1140),'white')
  for j,item in enumerate(p[start:start+4]):
   img=Image.open(E/(item['file'][:-4]+'-'+suffix+'.png')).convert('RGB')
   assert img.width==500 and img.height==570
   sheet.paste(img,((j%2)*500,(j//2)*570))
  sheet.save(E/f'{kind}-contact-{start//4+1:02}.png')
print(json.dumps({'verified_artifacts':len(p)*4,'unchanged_solution_hashes':len(a['solutionChecks']),'contact_sheets':18,'geometry_failures':len(a['geometryFailures'])}))
