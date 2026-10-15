// Isolated 35-figure harness using the verified read-only converter.
import path from 'node:path';
import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const scratch=path.join(process.env.HOME,'.hermes/profiles/curriculum-dev/cache/scratch/ds-diagrams-extra-16-21');
process.env.DIAGRAM_PLACEMENTS=path.join(here,'placements-extra-16-21.json');
process.env.DIAGRAM_AUDIT=path.join(here,'audit-extra-16-21.json');
process.env.DIAGRAM_EVIDENCE_DIR=scratch;
const placements=JSON.parse(await fs.readFile(process.env.DIAGRAM_PLACEMENTS,'utf8'));
for(const p of placements){
  if(p.local_svg!==`${p.lesson}/${p.file}` || p.local_editable!==`${p.lesson}/${p.editable}`)
    throw new Error(`Copies must be directly beside lesson.md: ${p.lesson}`);
}
await import('./build-first-half.mjs');
const audit=JSON.parse(await fs.readFile(process.env.DIAGRAM_AUDIT,'utf8'));
audit.scope='All 35 additional plan entries in modules 16–21; plan has no module 21 entries.';
audit.solutionChecks=JSON.parse(await fs.readFile(path.join(scratch,'solution-traces.json'),'utf8'));
for(const diagram of audit.diagrams){
  const p=placements.find(p=>p.file===diagram.file);
  diagram.local_svg=p.local_svg;
  diagram.local_editable=p.local_editable;
}
await fs.writeFile(process.env.DIAGRAM_AUDIT,JSON.stringify(audit,null,2)+'\n');
