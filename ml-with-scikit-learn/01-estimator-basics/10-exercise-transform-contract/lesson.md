---
title: "Exercise: separate fit from transform"
slug: "exercise-transform-contract"
order: 10
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use a supplied training-only StandardScaler to trace fit_transform and transform without relearning statistics."
seo_title: "Exercise: separate fit from transform | Scikit-Learn"
seo_description: "Use a supplied training-only StandardScaler to trace fit_transform and transform without relearning statistics in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "transform contract"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
---

# Exercise: separate fit from transform

Apply an already fitted scaler to a new product matrix with two feature columns. Unlike the one-column demo, the saved `mean_` and `scale_` now each contain two values. Broadcasting applies each statistic to its corresponding column.

The helper receives the fitted scaler and the query matrix. Use those arguments directly and return the transformed matrix. The training fit is supplied; repeating it inside the helper would erase the boundary this exercise asks you to preserve.

Run before editing and inspect the printed state. After implementation, the transformed query should have three rows and two columns, and the training means printed before and after should match. A query outside the training range is allowed to produce a large transformed value; that is not a reason to relearn the scaler.

## Data used here

`X_train` and `query`: float width in cm followed by float volume in liters, known before listing; no target is used. Rows describe synthetic products and contain no missing values.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Transform `query` with the already fitted scaler, returning the transformed matrix without learning new statistics.
