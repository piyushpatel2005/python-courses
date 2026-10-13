---
title: "Exercise: predict new rows"
slug: "exercise-new-predictions"
order: 6
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Predict on a new two-dimensional feature matrix with the fitted estimator."
seo_title: "Exercise: predict new rows | Scikit-Learn"
seo_description: "Predict on a new two-dimensional feature matrix with the fitted estimator in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "new predictions"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
---

# Exercise: predict new rows

Use the fitted width/price model on three new widths. The query count and units differ from the demo, but the prediction contract is unchanged: every query row has the trained feature schema and receives one estimate.

Implement `predict_rows` using the model argument. Do not build a second estimator or read the global training arrays inside the helper. Returning a stored prediction vector could look right for one Run and fail as soon as a query changes.

The supplied probe shows the query shape next to your result. Once implemented, compare their lengths and consider which query is outside the observed width range. That estimate is extrapolation. The exercise checks that you call the existing model correctly, not whether the tiny synthetic line is a useful price model.

## Data used here

`X_train` and `query`: float product widths in cm known before listing; `y_train`: float listed prices in USD. Query prices are unknown. No values are missing.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return `model.predict(query)` for every row of the two-dimensional query matrix without fitting the model again.
