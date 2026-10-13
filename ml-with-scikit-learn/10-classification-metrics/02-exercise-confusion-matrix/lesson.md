---
title: "Exercise: count classification outcomes"
slug: "exercise-confusion-matrix"
order: 2
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Build confusion_matrix with explicit label order and calculate accuracy."
seo_title: "Exercise: count classification outcomes"
seo_description: "Build confusion_matrix with explicit label order and calculate accuracy."
seo_keywords:
  - "scikit-learn"
  - "confusion-matrix"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

The demo uses synthetic furniture-return decisions; this exercise uses a different kitchenware flag table.

## Dataset

`observations.csv` contains 96 original synthetic HomeHurray Inc. observations. One independent synthetic measurement observation per row. These are teaching data, not actual company performance.

| Column | Meaning and type / unit | Availability / role |
|---|---|---|
| `observation_id` | Unique string observation ID | Audit metadata, excluded from X |
| `measurement_a` | Float synthetic measurement, arbitrary signed units | Available before the synthetic outcome; feature |
| `measurement_b` | Float synthetic measurement, arbitrary signed units | Available before the synthetic outcome; feature |
| `measurement_c` | Float synthetic measurement, arbitrary signed units | Available before the synthetic outcome; feature |
| `truth` | Integer 0/1 synthetic outcome; 1 is positive | Observed label used for metric arithmetic |
| `predicted` | Fabricated integer 0/1 decision | Supplied prediction, not an input feature |
| `score` | Fabricated float in [0, 1], larger favors class 1 | Supplied score, not an input feature |

All stored values are complete. The fixed observation snapshot is 2025-01-15. The values retain their original seeded-fixture order and precision. Decisions and scores were deliberately fabricated from labels to practice metrics; they are not independent fitted-model evaluation. Figures use separate tiny illustrative counts.

The supplied setup reads the real read-only CSV tab with `pd.read_csv(..., float_precision="round_trip")` and retains pandas tables until the metric, split, or estimator operation. Data loading is supplied; edit only `main.py` for the task. The complete maintainer dictionary is stored beside the lesson in `data-dictionary.md`.

HomeHurray Inc. compares synthetic return flags with observed outcomes. A confusion matrix counts rows, not probabilities. In `confusion_matrix`, rows are actual classes and columns are predicted classes. Pass `labels=[negative, positive]` explicitly: alphabetical label order is not a business definition of positive.

The four cells are true negatives (TN), false positives (FP), false negatives (FN), and true positives (TP), read row by row. The diagonal counts correct decisions. Accuracy can look high when almost every order belongs to one class, so retain the matrix alongside it.

The function signature and Run probe are supplied. Implement the behavior for its arguments, not only the visible fixture; Submit also checks changed inputs.

## A small calculation

$$
\mathrm{accuracy}=\frac{TP+TN}{n}
$$

Here $n$ is the number of observations. For the six-row illustration, $(2+2)/6=0.6667$ (rounded).

## Your Tasks

1. Return `(matrix, accuracy)` from `summarize`, preserving the supplied label order and counting correct predictions over all rows.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial helper returns `None` safely; a completed helper should return the stated result for new inputs too.
