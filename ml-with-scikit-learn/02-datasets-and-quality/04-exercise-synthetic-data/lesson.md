---
title: "Exercise: generate controlled datasets"
slug: "exercise-synthetic-data"
order: 4
language: "python"
lesson_type: "coding"
runtime: "pyodide"
summary: "Use make_regression and make_classification with explicit sizes and seeds."
seo_title: "Exercise: generate controlled datasets | Scikit-Learn"
seo_description: "Use make_regression and make_classification with explicit sizes and seeds in a different-data Python exercise."
seo_keywords:
  - "scikit-learn"
  - "synthetic data"
  - "Python"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
---

# Exercise: generate controlled datasets

Create a different synthetic fixture for a two-class problem. The previous demo generated continuous regression targets from two features; this exercise asks for three input columns and discrete labels from `make_classification`.

The generator call has already been explained in the demo. Use the helper's `seed` and `n_rows` arguments, and state the requested settings explicitly. In particular, zero redundant features leaves room for two informative columns within the three-column matrix. The remaining column does not carry the generated class signal.

Run should print `(100, 3)` for the visible feature shape and `(100,)` for its targets. Repeating a call with the same seed should keep the values stable. A helper that always uses 29 is still wrong, even though the visible call requests that value: callers must be able to request another reproducible fixture.

## Data used here

`X`: three float, unitless generated feature columns; `y`: integer synthetic class 0 or 1. All features are conceptually available before the artificial label; the stationary teaching snapshot is 2025-01-15. No values are missing. Class labels are not real return outcomes, and the fixture contains no customer identifiers.

Edit `main.py`, press Run to inspect the supplied probe, then Submit to check the behavior.

## Your Tasks

1. Implement `generate(seed, n_rows)` using `make_classification` with `n_rows` samples, three features, two informative features, zero redundant features, two classes, and `random_state=seed`.
