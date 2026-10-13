---
title: 'Exercise: compose preprocessing and prediction'
slug: exercise-pipeline
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Build Pipeline with a transformer followed by a regressor and predict raw
  rows.
seo_title: 'Exercise: compose preprocessing and prediction | Scikit-Learn'
seo_description: Build Pipeline with a transformer followed by a regressor and predict
  raw rows with a different practice fixture.
seo_keywords:
  - scikit-learn
  - pipeline
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - pandas
---

Use the supplied synthetic kitchenware sizes and material labels. Both a missing measurement and a new material occur in the query. Those are transform-time cases; do not append queries to training before fitting.

The double nesting has a practical purpose: operations that happen in sequence stay together, while operations on different columns run in separate branches. Call `fit(training, target)` on the outer pipeline, not on individual transformers with the full dataset. This lesson asks for that one boundary. It does not compare models or establish pricing quality.

## Your Tasks

1. Implement `fit_prices(training, target)` to fit and return an outer `Pipeline` with the supplied `preprocessor()` and a `LinearRegression(n_jobs=1)` final estimator. Pass raw training rows into `fit`.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
