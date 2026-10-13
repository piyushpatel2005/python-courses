---
title: "Exercise: choose a decision threshold"
slug: "exercise-thresholds"
order: 8
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Select a threshold from a fixed validation-only candidate set under a stated recall constraint."
seo_title: "Exercise: choose a decision threshold"
seo_description: "Select a threshold from a fixed validation-only candidate set under a stated recall constraint."
seo_keywords:
  - "scikit-learn"
  - "thresholds"
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

A probability score becomes a flag only after a threshold is chosen. The rule here is `score >= threshold`, so a score exactly on the boundary is positive. Lower thresholds generally flag more orders, but the precision change is not guaranteed to be monotonic.

Use only reserved validation labels to compare 0.3, 0.5, and 0.7. Among candidates with recall at least 0.75, choose the highest precision, then the highest threshold. If none meets the constraint, choose highest recall, then precision, then the lowest threshold. These tie rules make the policy reproducible. Freeze both the fitted scoring model and this threshold before opening the final test set; refitting would change the scores.

The function signature and Run probe are supplied. Implement the behavior for its arguments, not only the visible fixture; Submit also checks changed inputs.

## Your Tasks

1. Implement the stated validation-only threshold policy in `choose_threshold`, including the inclusive boundary and deterministic fallback.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial helper returns `None` safely; a completed helper should return the stated result for new inputs too.
