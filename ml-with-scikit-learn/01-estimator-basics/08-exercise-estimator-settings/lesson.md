---
title: "Exercise: inspect estimator settings"
slug: "exercise-estimator-settings"
order: 8
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use get_params and set_params without confusing settings with fitted attributes."
seo_title: "Exercise: inspect estimator settings | Scikit-Learn"
seo_description: "Use get_params and set_params without confusing settings with fitted attributes in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "estimator settings"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
---

# Exercise: inspect estimator settings

Configure the estimator supplied for a width/price example. The caller may have settings besides `fit_intercept`, so your helper should modify the existing object rather than replace it with a new `LinearRegression`.

The task does not ask you to fit anything. `configure` should enable the intercept and return the same estimator; the supplied code performs the subsequent training call and prints its learned intercept. That separation lets another caller reuse the helper with different data.

Use `get_params()` while inspecting the result if you want to confirm the configuration. Do not confuse the dictionary key `fit_intercept` with the learned attribute `intercept_`. The former is available before fitting, while the latter is produced by fitting.

## Data used here

`X_train`: float product width in cm known before listing; `y_train`: later float listed price in USD. All rows are complete.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Use `set_params` to enable `fit_intercept` on the supplied estimator and return that same estimator without fitting it or changing its other settings.
