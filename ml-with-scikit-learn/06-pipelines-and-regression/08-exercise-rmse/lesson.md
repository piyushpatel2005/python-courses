---
title: 'Exercise: measure squared-error sensitivity'
slug: exercise-rmse
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: Compute root_mean_squared_error and compare its response to one large miss
  with MAE.
seo_title: 'Exercise: measure squared-error sensitivity | Scikit-Learn'
seo_description: Compute root_mean_squared_error and compare its response to one large
  miss with MAE with a different practice fixture.
seo_keywords:
  - scikit-learn
  - rmse
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
---

For three lamp-price estimates, two misses are small and the third is much larger. The supplied MAE call provides a comparison, not a second task. Your result should come from the arguments rather than the visible array constants.

The supplied probe prints both metrics on identical validation rows. You change only the RMSE calculation. No training or refitting belongs inside this helper.

## Your Tasks

1. Implement `rmse_value(actual, predicted)` to return root mean squared error as a scalar in the target unit.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
