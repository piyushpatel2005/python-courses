---
title: Expand a feature representation
slug: polynomial-features
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: Use PolynomialFeatures(degree=2,include_bias=False) before scaling and Ridge.
seo_title: Expand a feature representation | Scikit-Learn
seo_description: Use PolynomialFeatures(degree=2,include_bias=False) before scaling
  and Ridge in an editable worked example.
seo_keywords:
  - scikit-learn
  - polynomial features
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
---

Let a linear regressor use squared terms and interactions without changing the original raw input table.

`PolynomialFeatures(degree=2, include_bias=False)` creates all monomials up to degree two. For two inputs it returns the original columns, their squares and their interaction. It does not fit a regression model and it does not create new observations.

`include_bias=False` avoids adding a column of ones because the later Ridge estimator already fits an intercept. The supplied pipeline places expansion before scaling and Ridge. This order gives each expanded term its own training mean and scale. During prediction the fitted expansion and scaler transform the raw queries in exactly the same way.

Degree changes the hypothesis space. More terms can fit curvature, but they can also overfit; validate that choice rather than judging training error alone. This task isolates degree-two expansion. Inspect `get_feature_names_out()` alongside the transformed row so the interaction is not mistaken for a second square.

Two raw features $a,b$ expand to $(a,b,a^2,ab,b^2)$.

$$
a=2,\ b=3\quad\Rightarrow\quad(2,3,4,6,9).
$$

The interaction $ab=6$ depends on both inputs; it is not another independent observation.

One two-feature query now produces five values. The number of rows stays the same; expansion changes columns, not samples.

![[a,b] expands to [a,b,a^2,ab,b^2]](polynomial-features-data-flow.svg)

## Your Tasks

1. Change the expansion degree from 1 to 2 in `expand_terms`; keep the bias column disabled.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
