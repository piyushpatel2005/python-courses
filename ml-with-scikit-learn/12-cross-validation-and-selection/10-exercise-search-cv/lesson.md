---
title: "Exercise: search a bounded parameter space"
slug: "exercise-search-cv"
order: 10
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use GridSearchCV with nested step parameters and compare RandomizedSearchCV as a bounded sampling alternative."
seo_title: "Exercise: search a bounded parameter space"
seo_description: "Use GridSearchCV with nested step parameters and compare RandomizedSearchCV as a bounded sampling alternative."
seo_keywords:
  - "scikit-learn"
  - "search-cv"
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

GridSearchCV compares each listed setting on the same development folds. `ridge__alpha` means the `alpha` parameter of the pipeline step named `ridge`; the double underscore reaches inside the pipeline. Each candidate fold refits imputation and scaling using only that fold's training rows.

With `refit=True`, the winner is then fitted on all rows passed to `fit`, not on any separately reserved final test. `best_score_` is a selection score and is optimistic as an evaluation of the selection process. RandomizedSearchCV is a bounded alternative: `n_iter` samples a fixed number of settings from distributions or lists rather than enumerating a grid. It still needs the same whole-pipeline and holdout boundaries.

The function signature and Run probe are supplied. Implement the behavior for its arguments, not only the visible fixture; Submit also checks changed inputs.

## A small calculation

$$
N_{\mathrm{fits}}=C K+1
$$

$N_{\mathrm{fits}}$ counts model fits.

$C$ is candidate count and $K$ is fold count. Three candidates and three folds require $3\times3+1=10$ fits including the final refit.

## Your Tasks

1. Return a fitted GridSearchCV over Ridge alpha `[0.1, 1.0, 10.0]`, using three seed-17 shuffled folds, negative MAE, serial execution, and refitting.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit. The initial helper returns `None` safely; a completed helper should return the stated result for new inputs too.
