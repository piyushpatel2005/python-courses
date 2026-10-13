---
title: "Exercise: arrange features and targets"
slug: "exercise-xy-shapes"
order: 2
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Construct X as samples by features and y as one target per row."
seo_title: "Exercise: arrange features and targets | Scikit-Learn"
seo_description: "Construct X as samples by features and y as one target per row in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "xy shapes"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
---

# Exercise: arrange features and targets

Build a feature/target pair for a different synthetic listing table. Here width and height are the predictors, and the last column contains listed price. There are five rows instead of four, so a solution tied to a fixed row count will not transfer.

The preceding demo selected two columns without moving any rows. Apply that same rule inside `make_xy`, using its argument rather than the global fixture. Return the arrays; the supplied probe handles printing. While the helper returns `None`, Run explains what is unfinished instead of trying to unpack it.

Check that the first width and height still correspond to the first price. Do not sort prices independently, flatten the feature matrix, or include price as a third feature. The tests call your helper with other row counts and values, because constructing aligned arrays is the goal, not reproducing one visible output.

## Data used here

`records[:, 0]`: float item width in cm; `records[:, 1]`: float item height in cm; both known before listing. `records[:, 2]`: float listed price in USD, the target assigned after measurement. Row position identifies the pairing and is not a feature. No values are missing.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Return `(X, y)` from `make_xy(records)`: the first two columns form a two-dimensional feature matrix and the last column forms a one-dimensional target, in the original row order.
