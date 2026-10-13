---
title: 'Exercise: read linear regression coefficients'
slug: exercise-linear-coefficients
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Explain intercept and conditional coefficient units without causal claims.
seo_title: 'Exercise: read linear regression coefficients | Scikit-Learn'
seo_description: Explain intercept and conditional coefficient units without causal
  claims with a different practice fixture.
seo_keywords:
  - scikit-learn
  - linear coefficients
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

The transfer model has three feature columns rather than two. Use the vector operations to preserve column alignment. The fixed CSV uses centered dimensionless features and arbitrary target units, not physical product measurements; its bias shifts the target intercept.

The supplied estimator is already fitted on the training portion of the synthetic CSV. Your helper reconstructs predictions from its learned attributes on new rows. Matrix multiplication combines one query row with the coefficient vector and returns one number per row. If you later scale inputs, the coefficients belong to those scaled units instead of raw kilograms or liters.

## Dataset

`regression-measurements.csv` contains **90 fixed synthetic rows**. The supplied code reads the real CSV with `pd.read_csv`, then selects a feature DataFrame and a separate target Series. Keep those labeled pandas objects through splitting; estimators accept them directly. Each row is one independent synthetic measurement observation. These are dimensionless teaching measurements, not observed HomeHurray sales, prices or customer outcomes. No values are missing.

| Columns | Type / unit | Availability and role |
|---|---|---|
| feature_1, feature_2, feature_3 | float, dimensionless | measured before label assignment; predictors |
| target_value | float, arbitrary target units | assigned after features; target only |

The CSV row position preserves the original fixture order. It is not a predictor or entity ID. The supplied split uses that same row order and seed as the worked example. The target must never appear in X. `float_precision="round_trip"` preserves saved numeric precision; file loading is supplied setup, not another task.

## Worked explanation

## Your Tasks

1. Implement `reconstruct(model, queries)` using the fitted intercept and coefficient vector. Return one prediction per query row without calling `predict` inside the helper.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
