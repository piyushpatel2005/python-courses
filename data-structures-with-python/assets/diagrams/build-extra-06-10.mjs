// Own entrypoint: reuse the read-only, verified SVG/native converter.
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
process.env.DIAGRAM_PLACEMENTS=path.join(here,'placements-extra-06-10.json');
process.env.DIAGRAM_AUDIT=path.join(here,'audit-extra-06-10.json');
process.env.DIAGRAM_EVIDENCE_DIR=path.join(process.env.HOME,'.hermes/profiles/curriculum-dev/cache/scratch/data-structures-extra-06-10');
await import('./build-first-half.mjs');
