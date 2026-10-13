---
title: 'Exercise: fit a linear support-vector classifier'
slug: exercise-linear-svm
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: Use LinearSVC(dual='auto') in a scaled pipeline and distinguish decision_function
  from probability.
seo_title: 'Exercise: fit a linear support-vector classifier | Scikit-Learn'
seo_description: Use LinearSVC(dual='auto') in a scaled pipeline and distinguish decision_function
  from probability with a different practice fixture.
seo_keywords:
  - scikit-learn
  - linear svm
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

The transfer fixture has three informative features and one cluster per class. Its scores can be larger than one or smaller than zero. Leave the supplied score-printing probe unchanged and return the fitted pipeline.

The CSV was created with a fixed `make_classification` call: three informative numeric features, no redundant ones, and two synthetic classes. `class_sep` controls separation while `random_state` makes the draw reproducible. These dimensionless rows are a teaching example, not measured customer behavior. Unlike logistic regression, this estimator does not provide `predict_proba`. Never clip its scores to the interval zero to one and call them probabilities.

## Dataset

`classification-measurements.csv` contains **100 fixed synthetic rows**. The supplied code reads the real CSV with `pd.read_csv`, then selects a feature DataFrame and a separate target Series. Keep those labeled pandas objects through splitting; estimators accept them directly. Each row is one independent synthetic measurement observation. These are dimensionless teaching measurements, not observed HomeHurray sales, prices or customer outcomes. No values are missing.

| Columns | Type / unit | Availability and role |
|---|---|---|
| feature_1, feature_2, feature_3 | float, dimensionless | measured before label assignment; predictors |
| class_label | integer, classes 0 and 1 | assigned after features; target only |

The CSV row position preserves the original fixture order. It is not a predictor or entity ID. The supplied split uses that same row order and seed as the worked example. The target must never appear in X. `float_precision="round_trip"` preserves saved numeric precision; file loading is supplied setup, not another task.

## Worked explanation

## Your Tasks

1. Implement `fit_margin(training, labels, C)` to fit a `scale` → `model` pipeline with `LinearSVC(C=C, dual="auto", max_iter=5000, random_state=17)`.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
