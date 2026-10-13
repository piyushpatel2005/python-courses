---
title: 'Exercise: produce sparse coefficients with Lasso'
slug: exercise-lasso
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Fit a scaled Lasso and inspect exact zeros without treating them as proven
  irrelevance.
seo_title: 'Exercise: produce sparse coefficients with Lasso | Scikit-Learn'
seo_description: Fit a scaled Lasso and inspect exact zeros without treating them
  as proven irrelevance with a different practice fixture.
seo_keywords:
  - scikit-learn
  - lasso
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

The transfer CSV preserves five generated features, three with signal, and additional target noise. That knowledge belongs to the synthetic fixture, not a rule that a fitted Lasso must recover exactly three nonzero coefficients.

A zero coefficient says that this fit did not use that scaled feature under this penalty. It does not prove the feature is irrelevant, and correlated inputs may substitute for one another. Scaling belongs inside the training-fitted pipeline. The probe reports coefficients and validation MAE, not a promised selected feature set. `max_iter=5000` and a tighter tolerance allow this small coordinate-descent fit to settle without turning iteration count into the lesson task.

## Dataset

`regression-measurements.csv` contains **100 fixed synthetic rows**. The supplied code reads the real CSV with `pd.read_csv`, then selects a feature DataFrame and a separate target Series. Keep those labeled pandas objects through splitting; estimators accept them directly. Each row is one independent synthetic measurement observation. These are dimensionless teaching measurements, not observed HomeHurray sales, prices or customer outcomes. No values are missing.

| Columns | Type / unit | Availability and role |
|---|---|---|
| feature_1, feature_2, feature_3, feature_4, feature_5 | float, dimensionless | measured before label assignment; predictors |
| target_value | float, arbitrary target units | assigned after features; target only |

The CSV row position preserves the original fixture order. It is not a predictor or entity ID. The supplied split uses that same row order and seed as the worked example. The target must never appear in X. `float_precision="round_trip"` preserves saved numeric precision; file loading is supplied setup, not another task.

## Worked explanation

## Your Tasks

1. Implement `fit_lasso(training, target, alpha)` as a fitted `scale` → `lasso` pipeline. Use the requested alpha, `max_iter=5000` and `tol=1e-6`.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
