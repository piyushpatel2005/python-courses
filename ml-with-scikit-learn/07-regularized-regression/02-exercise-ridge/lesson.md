---
title: 'Exercise: shrink coefficients with Ridge'
slug: exercise-ridge
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Fit a scaled Ridge pipeline and compare two alpha values on validation only.
seo_title: 'Exercise: shrink coefficients with Ridge | Scikit-Learn'
seo_description: Fit a scaled Ridge pipeline and compare two alpha values on validation
  only with a different practice fixture.
seo_keywords:
  - scikit-learn
  - ridge
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

The transfer CSV has four correlated synthetic measurements and a different noise level. It was generated with effective rank 2 to supply overlapping feature information. Its arbitrary units do not represent actual product data.

The default fitted intercept is not penalized. Ridge often shares weight among correlated features instead of forcing one coefficient exactly to zero. Inspecting a coefficient norm can describe shrinkage, but it does not measure business usefulness.

## Dataset

`regression-measurements.csv` contains **100 fixed synthetic rows**. The supplied code reads the real CSV with `pd.read_csv`, then selects a feature DataFrame and a separate target Series. Keep those labeled pandas objects through splitting; estimators accept them directly. Each row is one independent synthetic measurement observation. These are dimensionless teaching measurements, not observed HomeHurray sales, prices or customer outcomes. No values are missing.

| Columns | Type / unit | Availability and role |
|---|---|---|
| feature_1, feature_2, feature_3, feature_4 | float, dimensionless | measured before label assignment; predictors |
| target_value | float, arbitrary target units | assigned after features; target only |

The CSV row position preserves the original fixture order. It is not a predictor or entity ID. The supplied split uses that same row order and seed as the worked example. The target must never appear in X. `float_precision="round_trip"` preserves saved numeric precision; file loading is supplied setup, not another task.

## Worked explanation

## Your Tasks

1. Implement `fit_ridge(training, target, alpha)` to return a training-fitted pipeline named `scale` then `ridge`, using the requested alpha.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
