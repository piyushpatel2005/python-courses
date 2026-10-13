---
title: "Exercise: fill missing numerical values"
slug: "exercise-median-imputation"
order: 2
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Fit SimpleImputer(strategy='median') on training columns and reuse its statistics."
seo_title: "Exercise: fill missing numerical values | Scikit-Learn"
seo_description: "Fit SimpleImputer(strategy='median') on training columns and reuse its statistics in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "median imputation"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: fill missing numerical values

Impute missing width and volume measurements in a different product matrix. The missing positions differ from the demo, and the query includes a row missing both features. Fit one replacement per training column and reuse it for every query row.

## Dataset

**Row grain:** one synthetic product measurement. **Files:** `training.csv` (40 rows), `queries.csv` (3 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `width_cm` | Product width | float; cm | Input recorded before listing |
| `volume_l` | Packaged volume | float; liters | Input recorded before handling/listing |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. An empty numeric CSV cell means not recorded, not zero; pandas reads it as NaN. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return the fitted imputer with the transformed array. The supplied output shows `statistics_` before the completed query, which lets you connect a replacement to its training source. Use `keep_empty_features=True` so the helper also has a declared behavior for an entirely missing training column.

Do not calculate medians from the query or combine the partitions before fitting. A query-only outlier must not alter the replacements. Leave observed query values intact, preserve the row count, and keep the two feature columns in their original order.

The supplied setup reads `training.csv` (40 rows), `queries.csv` (3 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit `SimpleImputer(strategy="median", keep_empty_features=True)` on `train` only and return `(imputer, imputer.transform(query))`, retaining the feature columns even if one has no observed training values.
