# Source, data, and artwork provenance

## Original course material

The HomeHurray Inc. setting, explanations, exercises, quiz wording, product descriptions, synthetic CSV/JSON records, and SVG/Excalidraw figures were authored for this course. They are teaching artifacts, not real company records. No third-party course lesson, illustration, screenshot, logo, or exercise solution is intentionally reproduced. The named research courses informed scope and prerequisite decisions, not reusable content templates.

The course repository had no root LICENSE file when reviewed. This document does **not** assign a new license to the owner's original course, data, or artwork. The owner must choose any intended redistribution terms; do not label these originals MIT, CC0, or CC-BY merely because a referenced dependency uses an open license.

`dataset-inventory.json` names every learner-visible synthetic dataset with row count, columns, and SHA-256. Solution copies must match. Tiny inline fixtures and seeded generator examples are also original teaching data. Every file-backed lesson contains its own visible field dictionary, including missingness, feature/target/ID roles, and availability; project assets preserve additional full dictionaries. File counts refer to canonical learner files, not doubled solution copies or maintainer dictionary JSON.

`diagram-inventory.json` names every original SVG and editable scene and records their hashes and primitive types. The scenes contain separate vector elements, not flattened pictures. Generic chart shapes and mathematical expressions are drawn for these lessons; no outside course artwork is imported. See README for paired editing and visual revalidation.

## Bundled benchmark data

Benchmark observations are distinct from HomeHurray fixtures. Lessons call scikit-learn's bundled loaders rather than redistributing raw benchmark CSVs in this course. The scikit-learn software is BSD-3-Clause, but that software license does not determine all underlying dataset rights.[5]

- **Iris:** R. A. Fisher, Iris dataset, UCI DOI `10.24432/C56C76`. The UCI dataset page identifies CC BY 4.0.[7] The pinned `load_iris().DESCR` identifies Fisher's source and notes corrections relative to an older UCI version. Preserve that distinction rather than claiming all copies are byte-identical. The course uses the bundled corrected sample measurements, with task-specific row selection.
- **Wine:** Stefan Aeberhard and M. Forina (1992), Wine dataset, UCI DOI `10.24432/C5PC7J`; the UCI page identifies CC BY 4.0.[8] The pinned loader's description includes a conflicting generic creator field, but its original-owner passage identifies Forina and its references identify Aeberhard and collaborators. Use the dataset-specific attribution above, not that stray generic field. Lessons select chemical measurement columns and class labels; they do not turn these measurements into business records.
- **Digits:** E. Alpaydin and C. Kaynak (1998), Optical Recognition of Handwritten Digits, UCI DOI `10.24432/C50P49`; the UCI page identifies CC BY 4.0.[9] Scikit-learn's bundled digits are the dataset's test subset represented as 8-by-8 intensity grids. The PCA demo selects the first 240 bundled rows, splits them, and fits its projection on training only. Its exercise uses separate synthetic measurements.

The UCI attribution/license statements above were read from the primary dataset pages during integration; the loader-specific statements were checked against the installed scikit-learn 1.4.2 `DESCR` fields. Preserve citations and explain modifications when distributing derived benchmark material. This course does not grant permission on a third party's behalf.

## Topic research and reuse boundaries

The planning research record saved the source pages and these observed terms. These are attribution and editing boundaries, not a relicensing of this course:

| Reference | Observed terms | Use in this course |
|---|---|---|
| Inria scikit-learn MOOC | CC BY 4.0 in its repository license.[1] | Topic order, practical preprocessing, selection/evaluation distinctions; no imported notebooks or figures. |
| MIT Introduction to Machine Learning notes | CC BY-NC-SA 4.0 in its site footer.[2] | Concept and notation research; no copied prose, problem sets, or artwork. Do not assume a noncommercial/share-alike source permits unrestricted reuse. |
| ApX Getting Started with Scikit-Learn | Copyright notice; no open content license established by the planning review.[3] | Coverage comparison only. |
| ApX Building a Machine Learning Recommendation System | Copyright notice; no open content license established by the planning review.[4] | Content-ranking, temporal split, metric, and cold-start scope comparison only. |

For implementation details, use the scikit-learn **1.4** documentation matching the authored runtime, including common pitfalls, preprocessing, composition, model evaluation, cross-validation, grid search, feature extraction, calibration, clustering, and decomposition. The pinned browser package versions are in README. A newer documentation example is not proof an API exists in the current course runtime.

Keep provenance records when editing. If you import any future dataset, text, or figure, document its author, exact source/version, license, modification, and redistribution conditions before adding it. A link that returns HTTP 200 or a permissive software dependency license is not evidence of permission to copy unrelated content.

## Sources

[1] https://github.com/INRIA/scikit-learn-mooc/blob/main/LICENSE
[2] https://introml.mit.edu/notes
[3] https://apxml.com/courses/getting-started-with-scikit-learn
[4] https://apxml.com/courses/building-ml-recommendation-system
[5] https://github.com/scikit-learn/scikit-learn/blob/1.4.2/COPYING
[7] https://archive.ics.uci.edu/dataset/53/iris
[8] https://archive.ics.uci.edu/dataset/109/wine
[9] https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits
