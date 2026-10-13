---
title: "Exercise: scale with robust statistics"
slug: "exercise-robust-scaling"
order: 10
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Compare RobustScaler median/IQR with standard scaling on training outliers."
seo_title: "Exercise: scale with robust statistics | Scikit-Learn"
seo_description: "Compare RobustScaler median/IQR with standard scaling on training outliers in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "robust scaling"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: scale with robust statistics

Apply median/IQR scaling to width and volume with an extreme training product. The two-column fixture differs from the demo, and each feature needs its own median and percentile range.

## Dataset

**Row grain:** one synthetic product measurement. **Files:** `training.csv` (40 rows), `queries.csv` (3 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `width_cm` | Product width | float; cm | Input recorded before listing |
| `volume_l` | Packaged volume | float; liters | Input recorded before handling/listing |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. These files have complete values; no missing-value sentinel is present. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return the fitted `RobustScaler` and the transformed query. Leave the supplied standard-scaling comparison alone; it is setup for observing the difference, not a second learner task. The output row count must still equal the query row count, including the extreme product.

Read a robust-scaled value as an offset from the training median measured in training IQRs. Do not interpret it as a probability or as a cleaned measurement in the original unit. The tests vary both training and query arrays and check the learned median and IQR rather than requiring one memorized output.

The supplied setup reads `training.csv` (40 rows), `queries.csv` (3 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit `RobustScaler(quantile_range=(25, 75))` only on `train` and return the fitted scaler with its query transform, retaining every query row.
