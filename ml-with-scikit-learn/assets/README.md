# Maintaining Machine Learning with Scikit-Learn

This directory is maintainer documentation, not a lesson. The course has 178 coding lessons in 18 sections, arranged as 89 adjacent editable-demo/transfer-exercise pairs. Each lesson has one assessed behavior and one hidden synchronous Python test. Eighteen section quizzes contain five questions each. Keep `draft: true` in `../course.md` until the application acceptance gates are complete.

## Where to edit

- Edit `lesson.md` for explanations, task wording, metadata, and the visible data dictionary. A dictionary in this directory or a sibling file is not a substitute for the instruction-pane `Dataset` section.
- Edit `main.py`, `test_main.py`, and `solution/main.py` together when changing the task. Starters must Run safely but fail their assessment; references must pass. A demo asks for a small meaningful edit; its following exercise requires transfer to different observations.
- Keep `files.yaml` main-first. Explicitly list CSV/JSON tabs with `readonly: true`. File-backed solutions need their own matching manifest and byte-identical datasets. Hidden tests, dictionaries, figures, and editable scenes must not become editor tabs.
- Keep lesson slugs stable. Numeric folder prefixes and front-matter `order` must agree. `lesson-inventory.json` records every role, prerequisite, and task. Dependencies must point backward; pairs must remain adjacent. A quiz directory is not a lesson.
- Change the adjacent `.excalidraw` scene and `.svg` together. Each scene contains editable text, shapes, and connectors, not an embedded screenshot. SVG is the published image. Inspect both widths after changing either representation; text equality alone does not prove visual equivalence.

## Data and project invariants

`dataset-inventory.json` records the 163 learner-visible dataset files across 123 file-backed lessons (solution copies are additional files). `diagram-inventory.json` records 92 SVG/scene pairs. Three dense lessons now have a second, complementary visual: one mixed-table row, final-test isolation from cross-validation, and PCA projection with retained variance. Hashes describe the focused-review source snapshot, not a promise that future edits are already verified. `PROVENANCE.md` separates original synthetic data/artwork from benchmark data and outside research.

Small conceptual arrays, bundled Iris/Wine/Digits loaders, and explicit generator lessons stay small. Larger model examples use actual `pd.read_csv` or `pd.read_json` calls. Do not replace those reads with embedded strings or arrays. Retain DataFrames through table operations; use `.iloc` for positional row splits. Preserve precision, identifiers, row order, missing-value meanings, and split membership when editing fixtures.

The three exercise projects are cumulative, but each lesson is independently runnable:

| Project | Frozen contract |
|---|---|
| Listing prices | 120 products, snapshot 2025-01-15; 72 train / 24 validation / 24 test. Select alpha on validation; refit the fixed alpha on 96 development rows before the final 24-row report. Demos use 20 separate parcels. |
| Return risk | 180 independent orders, 108 search-training / 36 threshold-validation / 36 test. Thirty-day labels mature by 2025-04-01. Search only training; choose threshold on validation; do **not** refit after choosing that threshold. |
| Content recommendations | 18 fixed products, six users, 30 views. Metadata available 2025-01-01; three history events through January 19, validation January 26, test February 2. Keep profiles/popularity frozen, k=3, seen filtering, and ascending-ID tie breaks. Do not append validation events before testing. |

Copy completed previous exercise helpers unchanged into the next starter. Keep the same dataset bytes through every project stage and its solution. Teach any new API before a project asks for it. Reports need counts and limitations; they must not promise business gains from synthetic data.

## Safe regeneration policy

The checked-in lesson/data/figure files are authoritative. Earlier scratch builders predate CSV migration and subsequent review corrections. **Do not run an old author generator over this tree.** There is no supported one-command course regeneration.

For a figure change, duplicate the scene into a scratch directory, edit it with Excalidraw, and export an SVG there. Compare labels, values, shapes, and connectors with the current lesson and both source representations before replacing the matching pair. Export settings can change font metrics, so a successful export does not replace a 500px/360px visual check. Preserve separate original plot elements; do not flatten a chart into an image inside the scene.

For a dataset change, create the proposed CSV/JSON in scratch first. Compare types, row count, IDs, precision, missingness, and project split membership. Update visible dictionaries, canonical and solution files, and tests as one reviewed change. Recalculate examples rather than adjusting expected numbers by hand.

## Reproduce the portable source check

Use a dedicated virtual environment outside the course. The source validator does not overwrite lessons or generate replacement content. The optional native execution check uses a compatible scikit-learn environment; it does **not** establish Pyodide or application-UI acceptance.

```sh
COURSE=/absolute/path/to/python-courses/ml-with-scikit-learn
AUDIT=/absolute/path/to/your/scratch/sklearn-review
python3 -m venv "$AUDIT/venv"
"$AUDIT/venv/bin/python" -m pip install PyYAML numpy==1.26.4 scipy==1.12.0 pandas==2.2.0 scikit-learn==1.4.2 matplotlib==3.9.4
"$AUDIT/venv/bin/python" "$COURSE/assets/validate_course.py" --report "$AUDIT/structure.json"
MPLBACKEND=Agg "$AUDIT/venv/bin/python" "$COURSE/assets/validate_course.py" --run --report "$AUDIT/native.json"
```

The native Matplotlib version above is an audit convenience, not the browser version. The authored browser target is Pyodide 0.26.1 with scikit-learn 1.4.2, NumPy 1.26.4, SciPy 1.12.0, pandas 2.2.0, and Matplotlib 3.5.2. Recheck the actual application worker and package lock before upgrading APIs. Keep supported `n_jobs` settings at 1 and searches small.

The validator checks inventory, prerequisite direction, ordering, tabs/copies, visible filenames, task/test counts, figure companions, and quiz metadata. With `--run`, it checks every starter/reference against its hidden test and records stdout. This is a smoke test, not protection against every hardcoded answer. Also try wrong-method, changed-input, leakage, and boundary cases for the operation you changed.

## Application and publication checks

1. Copy the finished course into scratch and set only the **scratch copy** to `draft: false`. Run both real content loaders. Confirm 178 coding lessons, 178 hidden tests and references, 18 quizzes/90 parsed answers, correct ordered routes, and canonical readonly files. Do not publish to make a loader test pass.
2. Run the actual image copier from a scratch working directory with `CONTENT_DIR` pointing to the scratch content parent. Compare all 92 copied SVGs byte-for-byte.
3. Run the current production Pyodide worker and actual Submit grader with canonical datasets on every invocation. Save code/test/file/runner hashes and exact job IDs. Test fresh starts, repeated runs, reset restoration, and Run/Submit while a readonly data tab is active. A warm bootstrap is not a cold-start result.
4. In the full application, read final prose and equations at full/narrow widths, apply solutions through the UI, inspect task checkboxes, complete quizzes, and traverse Next links including module boundaries and revisits. Source parsing and a worker harness cannot establish these UI behaviors.
5. Keep failed and interrupted evidence. Report native execution, worker acceptance, Markdown rendering, image delivery, and full application walkthrough as separate scopes. Revalidate the rendered lesson after any prose edit and the runtime after any code/test/data or application-runner edit.

The integration evidence directory used for this review is the active profile scratch `sklearn-course/integration/`. It contains real-loader inventories, native results, calculations, fresh rendered images, source hashes, continuity checks, and an explicit acceptance-gap report. Scratch evidence is not shipped as learner content and may be pruned; archive it separately if needed.

The later `sklearn-course/focused-flow-review/` evidence records targeted prose/cohesion edits, a reproducible eight-lesson production-worker sample, and full/narrow inspection of three supplemental figures. The user deferred broad application E2E acceptance; those focused checks must not be labeled a full UI walkthrough.
