---
title: "Exercise: standardize numerical features"
slug: "exercise-standard-scaling"
order: 6
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Calculate StandardScaler training mean and population scale and transform a query."
seo_title: "Exercise: standardize numerical features | Scikit-Learn"
seo_description: "Calculate StandardScaler training mean and population scale and transform a query in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "standard scaling"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: standardize numerical features

Standardize a new three-feature fixture with the same training-only contract. The generator uses a different seed, row count, and width, so your helper must compute statistics from its argument instead of assuming two columns.

## Dataset

**Row grain:** one independent generated observation. **Files:** `training.csv` (100 rows), `queries.csv` (3 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `feature_0` | Generated feature 0 | float; unitless | Input; original column order |
| `feature_1` | Generated feature 1 | float; unitless | Input; original column order |
| `feature_2` | Generated feature 2 | float; unitless | Input; original column order |

Synthetic make_regression export: 100 samples, 3 features (all informative), noise=0, random_state=29. These are generated observations, not measured HomeHurray Inc. records. These files have complete values; no missing-value sentinel is present. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return the fitted scaler and the query transform. The supplied probe displays the saved means and scales before the query matrix. Each printed statistic belongs to the column in the same position; no target values are involved in this operation.

The tests include a constant training column. Use the library's default behavior rather than manually dividing by a standard deviation that might be zero. They also replace the query with extreme values while keeping training fixed, because saved preprocessing state must not depend on which future batch is being transformed.

The supplied setup reads `training.csv` (100 rows), `queries.csv` (3 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit a default `StandardScaler` on `train` only, with both centering and standard-deviation scaling enabled, and return the scaler and its transformed query matrix.
