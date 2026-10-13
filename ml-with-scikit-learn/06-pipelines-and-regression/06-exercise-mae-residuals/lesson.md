---
title: 'Exercise: read residuals and absolute error'
slug: exercise-mae-residuals
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: Compute residuals and mean_absolute_error on validation rows.
seo_title: 'Exercise: read residuals and absolute error | Scikit-Learn'
seo_description: Compute residuals and mean_absolute_error on validation rows with
  a different practice fixture.
seo_keywords:
  - scikit-learn
  - mae residuals
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
---

The transfer fixture has four synthetic shelf-price estimates, with both error signs. Return the full residual vector so a caller can later plot individual errors; do not replace it with absolute values.

The editor supplies synthetic validation predictions, so computing a metric does not fit any estimator. In a modeling workflow these predictions must come from a model trained without those validation targets. Use validation for comparison; keep final test errors out of this selection loop.

## Your Tasks

1. Implement `error_report(actual, predicted)` to return `(residuals, mae)`, using observed minus predicted for residuals and mean absolute error for the scalar.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
