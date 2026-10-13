---
title: "Exercise: measure a simple baseline"
slug: "exercise-holdout-baselines"
order: 10
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use DummyRegressor or DummyClassifier with a task-appropriate explicitly introduced metric."
seo_title: "Exercise: measure a simple baseline | Scikit-Learn"
seo_description: "Use DummyRegressor or DummyClassifier with a task-appropriate explicitly introduced metric in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "holdout baselines"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
---

# Exercise: measure a simple baseline

Build a majority-class baseline for a different synthetic checkout fixture. The preceding demo predicted a continuous mean; this exercise predicts the most frequent training label using `DummyClassifier`.

## Dataset

**Row grain:** one synthetic checkout. **Files:** `training.csv` (75 rows), `validation.csv` (25 rows).

| Column | Meaning | Type / unit | Role / availability |
| --- | --- | --- | --- |
| `feature_0` | Generated feature 0 | float; unitless | Input; ignored by dummy |
| `target` | Return outcome | integer; 0/1 | Later classification target |

Original synthetic HomeHurray Inc. teaching data; no actual customer records or measured business-performance claims. These files have complete values; no missing-value sentinel is present. Training, validation, and query filenames describe supplied membership, not predictor columns.

## Worked explanation

Return `(model, accuracy)`. Fit only on the training arguments, predict the validation inputs, and compare those predictions with the validation labels using `accuracy_score`. The supplied probe prints the metric and several predictions, so the helper does not need its own print calls.

Read the result in the context of the label counts. Always predicting the majority class can correctly classify many rows without finding any minority examples. This exercise checks a fair reference procedure, not a promised accuracy. If validation labels change, the reported accuracy can change, but the training-learned predicted class must remain the same.

The supplied setup reads `training.csv` (75 rows), `validation.csv` (25 rows). Open the read-only data tabs to inspect the records; edit only `main.py`. `pd.read_csv` reads the actual CSV file into a DataFrame; selecting named columns and calling `to_numpy()` gives the arrays used by the estimator. Empty numeric cells become NaN. 

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return a `DummyClassifier(strategy="most_frequent")` fitted only on training arguments and its validation `accuracy_score`, computed from predictions for `X_valid`.
