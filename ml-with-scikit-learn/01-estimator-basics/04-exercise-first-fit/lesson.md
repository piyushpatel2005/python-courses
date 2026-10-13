---
title: "Exercise: fit an estimator"
slug: "exercise-first-fit"
order: 4
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Fit LinearRegression on supplied training-only observations and distinguish learned attributes from constructor settings."
seo_title: "Exercise: fit an estimator | Scikit-Learn"
seo_description: "Fit LinearRegression on supplied training-only observations and distinguish learned attributes from constructor settings in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "first fit"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
---

# Exercise: fit an estimator

Fit the supplied synthetic width/price observations rather than the package data from the demo. The helper receives both arrays, and it should return the fitted estimator itself. Returning only a coefficient would lose the model's prediction method and the remaining learned state.

Start by constructing `LinearRegression` with the requested settings, then call `fit` with the arguments. The first array has one feature column even though it is two-dimensional. The target is a separate vector. The probe prints learned attributes only after your helper returns a model, so the unfinished starter remains runnable.

Inspect how the intercept changes when the target contains a different fixed contribution. A fitted helper should respond to changed training targets; it should not assign the demo's coefficient and intercept manually. This exercise still teaches fitting rather than evaluation, and its training pattern is deliberately simple.

## Data used here

`X_train`: float item width in cm, known before listing; `y_train`: float listed price in USD assigned afterward. Each row is one synthetic product; values are complete.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Fit and return a `LinearRegression` with `fit_intercept=True` and `n_jobs=1`, using only the helper arguments `X_train` and `y_train`.
