# Second-half diagram build and editable sources

Scope: original `assets/diagram-plan.json` entries 20–39 only. No additional-plan entries or lesson prose are written.

## Rebuild

From the course root:

```sh
python3 assets/diagrams/build-second-half.py
node assets/diagrams/build-second-half.mjs
```

Python generates original SVGs, byte-identical lesson copies, placements and executable algorithm checks. Node converts all 20 SVGs into native Excalidraw scenes and writes byte-identical lesson copies. Node requires the actual locally installed Excalidraw 0.18.1, React, Vite and Playwright dependencies, plus installed Chrome. The default dependency location is `~/.hermes/profiles/curriculum-dev/cache/scratch/oop-excalidraw`; set `EXCALIDRAW_DEPS` to override. Dependencies are read only. Harness files and evidence are isolated in `~/.hermes/profiles/curriculum-dev/cache/scratch/ds-second-half`; set `EXCALIDRAW_SCRATCH` to override.

## Reusable helpers

- `second_half_renderer.py`: dependency-free `Drawing` primitives for native SVG text, grouped rectangles, array cells, tree nodes, edge paths and captions. Import `Drawing`; call `save(placement, course_root, canonical_directory)`. Inputs are explicit coordinates. It does not invent algorithm layouts.
- `second-half-native.mjs`: exports `convertAndValidate({source,name})`, a self-contained browser-side function passed to Playwright `page.evaluate`. It expects mounted `window.E` (actual Excalidraw library) and `window.api` (actual React editor API). The wrapper in `build-second-half.mjs` shows the complete local-only harness.

Supported SVG grammar: `rect`, centered single-line `text`, single-rectangle groups, and numeric M/L paths bearing `data-connector`. `data-arrow="true"` selects an arrowhead; plain tree/graph edges remain undirected. Extend the converter before using additional SVG geometry. Single-label groups use reciprocal text/container bindings; connector endpoints are reciprocally bound to matching rectangle edges. No raster/image elements are used.

The native converter loads its serialized JSON through `loadFromBlob`, mounts the result in the editor, exports SVG, programmatically edits a native text element through the editor API, exports again and reloads the edited JSON. This is real library/editor testing, not JSON-schema-only validation. Published companions retain original text, not the edit-test suffix. Source text equality is checked. Browser SVG text bounds and pairwise overlap are also checked.

## Evidence

`audit-second-half.json` holds per-diagram native element counts, import/edit/export/reload flags, copy comparisons and evidence paths. `placements-second-half.json` lists every canonical and lesson destination. `checks-second-half.json` records executable algorithm assertions.

The scratch evidence directory contains a 500px SVG render, actual editor screenshot, native-exported SVG and edited-export SVG for each diagram. Visual reviews inspect these images; automated checks do not replace visual review.

## Editing limitations

Text, boxes and connectors are genuine editable native elements. Background rectangles are locked intentionally. Arial-compatible Excalidraw font family 2 preserves the SVG geometry; native bold weight is not used. Longer text may require resizing a node or repositioning adjacent items; moving nodes with orthogonal multi-segment connectors may require manually adjusting bends. The drawings are illustrative data, never claims about exercise fixture names or expected output.
