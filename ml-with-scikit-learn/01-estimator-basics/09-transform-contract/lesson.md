---
title: "Separate fit from transform"
slug: "transform-contract"
order: 9
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use a supplied training-only StandardScaler to trace fit_transform and transform without relearning statistics."
seo_title: "Separate fit from transform | Scikit-Learn"
seo_description: "Use a supplied training-only StandardScaler to trace fit_transform and transform without relearning statistics with a small editable Python example."
seo_keywords:
  - "scikit-learn"
  - "transform contract"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
---

# Separate fit from transform

A transformer learns how to change a feature representation. It does not necessarily predict a target. `StandardScaler` is a transformer that stores a mean and scale for each feature column. This lesson follows its method calls; a later lesson works through the full arithmetic.

The supplied setup creates a scaler and calls `fit_transform(X_train)`. This combines learning statistics from the training rows with transforming those same rows. `fit` alone would learn the statistics without returning the transformed matrix. The learned values are available as `mean_` and `scale_`.

For new rows, call `transform(query)` on that fitted object. It uses the saved training statistics and preserves the number of rows and feature columns. The transformed values use a new numerical scale, but a row still describes the same package and a column still refers to the same measurement.

The starter deliberately calls `fit_transform` on the query. That method is valid Python and produces a result, but it replaces the training state with statistics from the query batch. Run and compare the printed means before and after. Once you use `transform`, those two means should agree even when the query contains a much larger weight.

This distinction matters whenever training and future data must use a common coordinate system. If every query batch learns a new mean, the same raw value can receive different transformed values depending on the other queries beside it. A fitted transformer should not change merely because you ask it to process a new batch.

These arrays are an interface demonstration rather than an evaluation experiment. They introduce state reuse before we build a formal training/validation split.

## Worked calculation

For a raw value $x$, training mean $\mu$, and training scale $s$, the transformed value is $z=(x-\mu)/s$. Here $\mu=4$ kg and $s\approx1.633$ kg.

$$
z(8)=\frac{8-4}{1.633}\approx2.449.
$$

The transformed value is dimensionless. The numeric-preprocessing module explains how the scaler computes $s$.

## Data used here

`X_train` and `query`: float package weights in kg, available before handling; no target is used. Each row is one synthetic package. Values are complete.

![Training: [2, 4, 6] kg. Query: [[4], [8]] kg. Same Feature, New Scale](transform-contract-data-flow.svg)

## Small edit

Replace the helper's `fit_transform(query)` with `transform(query)`.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Transform `query` with the already fitted scaler, returning the transformed matrix without learning new statistics.
