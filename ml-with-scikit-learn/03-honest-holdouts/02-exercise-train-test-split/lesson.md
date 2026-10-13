---
title: "Exercise: create a held-out test set"
slug: "exercise-train-test-split"
order: 2
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Split aligned row IDs X and y reproducibly before any learned preprocessing."
seo_title: "Exercise: create a held-out test set | Scikit-Learn"
seo_description: "Split aligned row IDs X and y reproducibly before any learned preprocessing in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "train test split"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: create a held-out test set

Split a different generated fixture with three features and IDs that begin at 500. The IDs deliberately differ from row positions: use them as data to partition, not as NumPy positions into another array.

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

Return the six arrays in `train_test_split`'s documented order. The probe handles unpacking and printing, so your task is the aligned split rather than a separate reporting function. With 100 rows and a quarter held out, Run should show 75 training rows and 25 test rows.

Do not split `X` and `y` independently, even if repeating the same seed might appear to work. Passing all aligned arrays through one split expresses the pairing directly and includes the audit IDs. Repeating your helper with unchanged inputs should reproduce the row assignments; it should not fit any transformation or estimator.

The supplied setup reads `observations.csv` (100 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return the six outputs of one `train_test_split(ids, X, y, ...)` call with `test_size=0.25` and `random_state=17`, preserving paired row values.
