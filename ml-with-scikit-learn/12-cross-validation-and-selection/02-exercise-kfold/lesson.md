---
title: "Exercise: evaluate whole pipelines in folds"
slug: "exercise-kfold"
order: 2
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use explicit KFold and cross_validate with neg_mean_absolute_error and report spread not a confidence interval."
seo_title: "Exercise: evaluate whole pipelines in folds"
seo_description: "Use explicit KFold and cross_validate with neg_mean_absolute_error and report spread not a confidence interval."
seo_keywords:
  - "scikit-learn"
  - "kfold"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
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

K-fold evaluation rotates which development rows are held out. `KFold` returns positional train/validation indices, not copies of data. With three folds, every row is validation once. Shuffling with a fixed seed is appropriate here because rows are independent synthetic product measurements.

Pass the entire impute-scale-Ridge pipeline to `cross_validate`; it clones and fits a fresh pipeline inside each fold. The scorer `neg_mean_absolute_error` returns negative error because search APIs maximize scores. Negate it to report positive MAE. Inspect the spread of fold errors, but do not call their standard deviation a confidence interval: training sets overlap. Final-test rows do not belong in this call. The returned key `test_score` names each fold's validation score; it does not mean that the separately reserved final test has been opened.

The function signature and Run probe are supplied. Implement the behavior for its arguments, not only the visible fixture; Submit also checks changed inputs.

## A small calculation

$$
e_j=-s_j
$$

$s_j$ is the negative-MAE scorer for fold $j$ and $e_j$ is its positive MAE. Scores $-2,-3,-4$ give mean MAE $(2+3+4)/3=3$ target units.

## Your Tasks

1. Return `(folds, positive_mae, estimators)` from three shuffled KFold splits with seed 17 and a fresh whole pipeline in each fold.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial helper returns `None` safely; a completed helper should return the stated result for new inputs too.
