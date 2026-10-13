---
title: "Exercise: vary the amount of training data"
slug: "exercise-learning-curves"
order: 12
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use learning_curve with a whole pipeline and read the training-size axis."
seo_title: "Exercise: vary the amount of training data"
seo_description: "Use learning_curve with a whole pipeline and read the training-size axis."
seo_keywords:
  - "scikit-learn"
  - "learning-curves"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "matplotlib"
  - "pandas"
---

The exercise uses a different synthetic kitchenware fixture from the demonstration.

## Dataset

`observations.csv` contains 96 original synthetic HomeHurray Inc. observations. One independent synthetic measurement observation per row. These are teaching data, not actual company performance.

| Column | Meaning and type / unit | Availability / role |
|---|---|---|
| `observation_id` | Unique string observation ID | Audit metadata, excluded from X |
| `measurement_a` | Float synthetic measurement, arbitrary signed units | Available before the synthetic outcome; feature |
| `measurement_b` | Float synthetic measurement, arbitrary signed units | Available before the synthetic outcome; feature |
| `target` | Float response in arbitrary simulation units | Observed synthetic target, excluded from X |

All stored values are complete. The fixed observation snapshot is 2025-01-15. The values retain their original seeded-fixture order and precision. The identifier and target stay outside the feature table. Query perturbations in tree lessons are interface probes, not an independent held-out evaluation. Currency figures are separate arithmetic illustrations.

The supplied setup reads the real read-only CSV tab with `pd.read_csv(..., float_precision="round_trip")` and retains pandas tables until the metric, split, or estimator operation. Data loading is supplied; edit only `main.py` for the task. The complete maintainer dictionary is stored beside the lesson in `data-dictionary.md`.

A learning curve changes the amount of training data while keeping model settings fixed. The x-axis is training-row count, not alpha or tree depth. `learning_curve` returns actual sizes and two matrices: one row per size and one column per fold.

Fractions such as 0.5 are relative to the maximum training portion within a fold, not the full dataset. Keep the whole pipeline inside the call so every subset learns its own preprocessing. Negate negative-MAE scores before averaging across columns. Comparing training and validation errors can suggest whether more data might help, but neither curve must improve monotonically on a small sample.

The function signature and Run probe are supplied. Implement the behavior for its arguments, not only the visible fixture; Submit also checks changed inputs.

## A small calculation

$$
\bar e_m=\frac{1}{K}\sum_{j=1}^{K}e_{m,j}
$$

$\bar e_m$ is the mean validation error at training size $m$.

$e_{m,j}$ is MAE at training size $m$ in fold $j$; $K$ is fold count. A row of errors 2, 3, and 4 has mean 3 target units.

## Your Tasks

1. Return actual training sizes and positive training/validation MAE matrices for fractions `[0.5, 0.75, 1.0]` across three seeded folds.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial helper returns `None` safely; a completed helper should return the stated result for new inputs too.
