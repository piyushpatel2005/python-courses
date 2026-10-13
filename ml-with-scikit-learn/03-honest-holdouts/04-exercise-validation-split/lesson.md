---
title: "Exercise: reserve validation data"
slug: "exercise-validation-split"
order: 4
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Split the development portion again so model choices never inspect final test targets."
seo_title: "Exercise: reserve validation data | Scikit-Learn"
seo_description: "Split the development portion again so model choices never inspect final test targets in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "validation split"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: reserve validation data

Build three disjoint ID partitions for the new 100-row fixture. The required overall shares remain 60% training, 20% validation, and 20% test. Only the first split operates on the full table.

## Dataset

**Row grain:** one independent generated observation. **Files:** `observations.csv` (100 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `row_id` | Original row identifier | integer; unitless | Audit/split alignment only; excluded from X |
| `feature_0` | Generated feature 0 | float; unitless | Input; original column order |
| `feature_1` | Generated feature 1 | float; unitless | Input; original column order |
| `feature_2` | Generated feature 2 | float; unitless | Input; original column order |
| `target` | Generated regression outcome | float; unitless | Target; excluded from X |

Synthetic make_regression export: 100 samples, 3 features (all informative), noise=5, random_state=29. These are generated observations, not measured HomeHurray Inc. records. These files have complete values; no missing-value sentinel is present. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Your helper should return `(train, validation, test)`. The supplied feature-shape probe uses the training positions but does not fit anything. Read its output as a boundary check: 60 training positions should select a `(60, 3)` feature matrix in this exercise.

A common mistake is to use 20% of the development portion for validation. That creates 16% of the original table instead of the requested 20%. Another mistake is to take validation rows from a fresh split of the original IDs, allowing overlap with the test set. Split the development IDs returned by the first call.

The supplied setup reads `observations.csv` (100 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return train, validation, and test IDs using two seeded splits: reserve 20% as test first, then reserve 25% of the remaining development IDs as validation; use `random_state=17` in both calls.
