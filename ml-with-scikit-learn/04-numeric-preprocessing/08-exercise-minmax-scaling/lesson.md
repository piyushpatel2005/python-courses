---
title: "Exercise: rescale to a training range"
slug: "exercise-minmax-scaling"
order: 8
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Fit MinMaxScaler and show that new values can fall outside the fitted range."
seo_title: "Exercise: rescale to a training range | Scikit-Learn"
seo_description: "Fit MinMaxScaler and show that new values can fall outside the fitted range in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "minmax scaling"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: rescale to a training range

Scale a new three-column fixture using only its training minima and maxima. The query deliberately includes values outside those observed ranges. Retain the out-of-range scaled values rather than clipping them.

## Dataset

**Row grain:** one independent generated observation. **Files:** `training.csv` (100 rows), `queries.csv` (3 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `feature_0` | Generated feature 0 | float; unitless | Input; original column order |
| `feature_1` | Generated feature 1 | float; unitless | Input; original column order |
| `feature_2` | Generated feature 2 | float; unitless | Input; original column order |

Synthetic make_regression export: 100 samples, 3 features (all informative), noise=0, random_state=29. These are generated observations, not measured HomeHurray Inc. records. These files have complete values; no missing-value sentinel is present. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

The helper should return both the fitted `MinMaxScaler` and its query transform. Do not calculate a fresh range from each query column; that would make the same raw input depend on what other rows happen to be submitted beside it.

Inspect the printed `data_min_` and `data_max_` arrays alongside the output. The endpoints belong to training columns in order. A new extreme should change its own output but leave the saved endpoints unchanged. A result outside 0–1 is consistent with this contract and helps distinguish new inputs from the fitted interval.

The supplied setup reads `training.csv` (100 rows), `queries.csv` (3 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit `MinMaxScaler(feature_range=(0, 1), clip=False)` on `train` only and return its fitted object and transformed query, allowing new values outside the training range to map outside 0–1.
