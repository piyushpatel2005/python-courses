---
title: "Exercise: preserve class representation"
slug: "exercise-stratified-holdout"
order: 6
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use stratify with enough samples per class and explain when random row splitting is inappropriate."
seo_title: "Exercise: preserve class representation | Scikit-Learn"
seo_description: "Use stratify with enough samples per class and explain when random row splitting is inappropriate in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "stratified holdout"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: preserve class representation

Stratify a new fixture with a different class mix. The table has 100 rows, including 40 positives, rather than the demo's 80 rows with 16 positives. Use the supplied labels as the stratification argument instead of constructing counts for one fixed dataset.

## Dataset

**Row grain:** one independent synthetic checkout. **Files:** `labels.csv` (100 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `row_id` | Original row identifier | integer; unitless | Audit/split alignment only; excluded from X |
| `label` | Return flag | integer; 0/1 | Later outcome; audit/stratification only |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. These files have complete values; no missing-value sentinel is present. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return training IDs followed by test IDs. The probe uses those positions to print each partition's two class counts. A quarter of the new table should contain 15 zeros and 10 ones, leaving 45 zeros and 30 ones in training.

Do not duplicate minority rows to force these counts. The partitions must remain disjoint and exhaustive. For an impossible request with only one observation in a class, allow `train_test_split` to raise its normal `ValueError`. That failure describes an inadequate split design rather than something to hide with a fallback.

The supplied setup reads `labels.csv` (100 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return a 25% holdout split of the IDs with `random_state=17` and `stratify=labels`; let the splitter raise `ValueError` when a class has too few observations.
