---
title: 'Exercise: fit a nonlinear SVM'
slug: exercise-rbf-svm
order: 10
language: python
lesson_type: coding
runtime: pyodide
summary: Use SVC(kernel='rbf') with small data and compare C/gamma on validation only.
seo_title: 'Exercise: fit a nonlinear SVM | Scikit-Learn'
seo_description: Use SVC(kernel='rbf') with small data and compare C/gamma on validation
  only with a different practice fixture.
seo_keywords:
  - scikit-learn
  - rbf svm
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

The transfer draw changes separation, seed and candidate values. Keep those supplied arrays separate. The function should work on another training geometry, not return whichever pair happened to win in the demo.

The generated two-feature data use two clusters per class to make a single linear boundary less suitable. RBF can represent more flexible relationships, but it may still lose on unseen rows. Keep test data outside the helper and do not enable probability estimation simply to get labels; ordinary `predict` already provides them.

## Dataset

`classification-measurements.csv` contains **120 fixed synthetic rows**. The supplied code reads the real CSV with `pd.read_csv`, then selects a feature DataFrame and a separate target Series. Keep those labeled pandas objects through splitting; estimators accept them directly. Each row is one independent synthetic measurement observation. These are dimensionless teaching measurements, not observed HomeHurray sales, prices or customer outcomes. No values are missing.

| Columns | Type / unit | Availability and role |
|---|---|---|
| feature_1, feature_2 | float, dimensionless | measured before label assignment; predictors |
| class_label | integer, classes 0 and 1 | assigned after features; target only |

The CSV row position preserves the original fixture order. It is not a predictor or entity ID. The supplied split uses that same row order and seed as the worked example. The target must never appear in X. `float_precision="round_trip"` preserves saved numeric precision; file loading is supplied setup, not another task.

## Worked explanation

## Your Tasks

1. Implement `select_rbf` to train one scaled RBF SVC per supplied `(C, gamma)` pair and return `(winning_pair, validation_accuracies)`. Maximize validation accuracy; choose the first exact tie.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
