---
title: "Exercise: keep learned statistics inside training"
slug: "exercise-preprocessing-leakage"
order: 8
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Fit a supplied scaler on training rows only and transform validation rows."
seo_title: "Exercise: keep learned statistics inside training | Scikit-Learn"
seo_description: "Fit a supplied scaler on training rows only and transform validation rows in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "preprocessing leakage"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: keep learned statistics inside training

Build a training-only scaling helper for two product features. Width and volume have different units, so the scaler learns a separate mean and scale for each column. The validation rows are intentionally larger than the training observations.

## Dataset

**Row grain:** one synthetic product measurement. **Files:** `training.csv` (40 rows), `queries.csv` (3 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `width_cm` | Product width | float; cm | Input recorded before listing |
| `volume_l` | Packaged volume | float; liters | Input recorded before handling/listing |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. These files have complete values; no missing-value sentinel is present. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return the fitted scaler together with its validation transform. This makes the learned boundary inspectable: the scaler should record 40 training observations, not 43 combined observations. The output should retain three rows and two columns.

Do not fit on validation, concatenate the partitions, or call `fit_transform` on validation after fitting training. All three can produce finite-looking numbers, but they let held-out inputs determine their own coordinate system. The helper must also respond to a different training matrix rather than storing one fixture's statistics.

The supplied setup reads `training.csv` (40 rows), `queries.csv` (3 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit a `StandardScaler` only on `train`, then return `(scaler, transformed_validation)` using that same fitted scaler to transform `validation`.
