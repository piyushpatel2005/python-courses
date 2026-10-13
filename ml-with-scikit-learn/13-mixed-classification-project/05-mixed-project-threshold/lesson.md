---
title: "Set an operational threshold"
slug: "mixed-project-threshold"
order: 5
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use a reserved validation partition to select a stated recall-constrained threshold after train-only CV."
seo_title: "Set an operational threshold"
seo_description: "Use a reserved validation partition to select a stated recall-constrained threshold after train-only CV."
seo_keywords:
  - "scikit-learn"
  - "mixed-project-threshold"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

The furniture analogue has a separate six-row validation slice. Its policy compares 0.25, 0.5, and 0.75, requiring recall at least 0.6 before maximizing precision. Feasible ties favor the highest threshold. If none qualifies, maximize recall then precision and favor the lowest threshold. These values differ from the checkout project.

## Dataset

`handling.csv` contains 30 original synthetic HomeHurray Inc. observations. One synthetic furniture-handling observation per row. These are teaching data, not actual company performance.

| Column | Meaning and type / unit | Availability / role |
|---|---|---|
| `weight_kg` | Float package weight, kg | Known before handling; numeric predictor |
| `width_cm` | Float width, cm | Known before handling; numeric predictor |
| `material` | Nominal wood / steel | Known before handling; categorical predictor |
| `flagged` | Integer 0/1 handling flag | Observed later; target |

A blank weight means an unrecorded measurement; other fields are complete. `glass` is an unseen query material, not a stored training category. The fixed observation snapshot is 2025-01-15. The supplied positional slices contain 18 training, 6 validation, and 6 final-test observations. This is a small standalone analogue, not the checkout project table.

The supplied setup reads the real read-only CSV tab with `pd.read_csv(..., float_precision="round_trip")` and retains pandas tables until the metric, split, or estimator operation. Data loading is supplied; edit only `main.py` for the task. The complete maintainer dictionary is stored beside the lesson in `data-dictionary.md`.

A score on the boundary counts as positive. Changing `>` to `>=` can therefore alter feasibility even though both expressions return Boolean arrays. Choose with validation only and retain the fitted scoring model unchanged.

![Search-training data separate from threshold-validation and final test](mixed-project-threshold-data-flow.svg)

The supplied additional checkpoint exposes the changed policy even when the main fixture produces the same prediction. It is a probe, not another task.

## Your Tasks

1. Change `scores > threshold` to `scores >= threshold` in `choose_threshold` so the analogue follows the described policy.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial demo runs but its setting does not yet meet the task. After the edit, compare the checkpoint with the original run.
