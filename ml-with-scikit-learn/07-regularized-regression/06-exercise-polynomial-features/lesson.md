---
title: 'Exercise: expand a feature representation'
slug: exercise-polynomial-features
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: Use PolynomialFeatures(degree=2,include_bias=False) before scaling and Ridge.
seo_title: 'Exercise: expand a feature representation | Scikit-Learn'
seo_description: Use PolynomialFeatures(degree=2,include_bias=False) before scaling
  and Ridge with a different practice fixture.
seo_keywords:
  - scikit-learn
  - polynomial features
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
---

The transfer queries use new feature values and contain two rows. Return all five degree-two terms for each row in the library order. The supplied regression pipeline demonstrates where expansion belongs, but your task concerns the transformation helper.

Degree changes the hypothesis space. More terms can fit curvature, but they can also overfit; validate that choice rather than judging training error alone. This task isolates degree-two expansion. Inspect `get_feature_names_out()` alongside the transformed row so the interaction is not mistaken for a second square.

## Your Tasks

1. Implement `expand_terms(training, queries)` to return the degree-two expanded query matrix and its output names. Exclude a bias column.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
