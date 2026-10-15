# Editable OOP diagram companions

The eight SVGs remain the canonical published images. Their `.excalidraw` companions are editable working sources, not lesson editor tabs. No `files.yaml` or lesson prose changes are required.

## Manual edits

1. Open the `.excalidraw` from this directory in a trusted local Excalidraw editor (File → Open). Do not use collaboration/share/upload for course content.
2. Select a card to move its grouped rectangle and text. Enter the group or ungroup to edit individual lines; double-click text to edit. Single-label cards have bound text; mixed-size multi-line cards use groups to retain separate heading/body sizes. All arrow ends are bound to their cards.
3. Background and blue header-rule rectangles are locked to avoid accidental movement; unlock if needed. Other rectangles, text, and arrows are editable.
4. Save the edited `.excalidraw` here, then copy it **byte-for-byte** beside the corresponding lesson listed in `../diagram-placements.json`. Keep these two copies identical.
5. Export SVG to a **new preview filename**, visually review, and separately decide whether/how to update the published SVG and `build_diagrams.py`. Editing this companion does not modify those files. Do not silently replace canonical SVGs with an Excalidraw export.

## Repeatable generation and acceptance checks

**Warning:** running the converter replaces all eight `.excalidraw` sources and eight lesson copies from the existing SVGs; back up manual edits first. It never writes SVGs or lesson prose. It is deliberately tailored to this SVG generator's rectangles, text, card groups, and M/L connector paths—not a general SVG importer.

Dependencies and test evidence stay outside the course, under the curriculum-dev scratch directory:

```sh
export EXCALIDRAW_SCRATCH="$HOME/.hermes/profiles/curriculum-dev/cache/scratch/oop-excalidraw"
mkdir -p "$EXCALIDRAW_SCRATCH"
npm install --prefix "$EXCALIDRAW_SCRATCH" @excalidraw/excalidraw@0.18.1 react@18.3.1 react-dom@18.3.1 vite@8.3.4 playwright@1.64.1
# Only if Playwright has no local Chromium:
"$EXCALIDRAW_SCRATCH/node_modules/.bin/playwright" install chromium
node build_excalidraw.mjs
```

The converter starts a loopback-only Vite server, mounts the actual React Excalidraw editor in headless Chromium, and blocks all browser requests outside 127.0.0.1. No course content is uploaded. Each file is constructed and serialized with the official library, imported through `loadFromBlob`, rendered by the editor, and exported with `exportToSvg`. A text element is then edited through the editor API, its exported SVG checked for the change, and the edited serialized file reimported; this test edit is not saved to the deliverable. Source text equality, native element types, element counts, and identical lesson copies are asserted.

Evidence: `$EXCALIDRAW_SCRATCH/evidence/report.json` records exact paths, versions, element/binding counts and acceptance outcomes; `*-editor.png` shows the actual editor; `*.svg` and `*-edited.svg` show library exports before/after the test edit. Scratch artifacts may eventually be pruned; rerun to reproduce. All eight screenshots were visually inspected, with the MRO diagram additionally inspected at full size.

## Fidelity and editing limitations

- All original text and fill/stroke colors are retained, with original card/connector geometry and centered text closely matched. There are no embedded SVG/image elements or external files.
- Excalidraw's Helvetica/Arial-style font (font family 2) matches the original sans-serif better than the hand-drawn font. Native Excalidraw text has no per-element bold weight here, so formerly bold headings render regular-weight. Font metrics/baseline, rounded-corner radii, and triangle arrowhead sizes differ slightly.
- Multi-line cards retain separate 21px headings and 19px body text as grouped native elements, not a single bound text block. Enlarging text does not automatically resize those cards; adjust the rectangle/group manually. Single-label card text is bound.
- Connector paths are native non-elbowed arrows, including the two bent class/instance connectors. End bindings are retained, but moving cards substantially can require manually adjusting bends and side annotations. This is a conceptual illustration, not UML.
- Existing published SVGs remain the pixel/layout reference; these editable companions are not pixel-identical substitutes.
