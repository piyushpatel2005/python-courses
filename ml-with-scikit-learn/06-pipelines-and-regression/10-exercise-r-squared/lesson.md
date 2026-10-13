---
title: 'Exercise: compare with a mean reference'
slug: exercise-r-squared
order: 10
language: python
lesson_type: coding
runtime: pyodide
summary: Calculate r2_score and explain zero negative values and constant-target caveats.
seo_title: 'Exercise: compare with a mean reference | Scikit-Learn'
seo_description: Calculate r2_score and explain zero negative values and constant-target
  caveats with a different practice fixture.
seo_keywords:
  - scikit-learn
  - r squared
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
---

A deliberately poor shelf-price predictor exceeds every target in this fixture. Preserve the negative result. A negative score says something about this evaluated comparison, not that the implementation should refuse the input.

For a constant target the denominator vanishes. The default `force_finite=True` replaces non-finite perfect/imperfect results with 1 or 0. With `force_finite=False`, those constant-target cases remain NaN or negative infinity. Report that limitation rather than interpreting the replacement as ordinary explained variation. This lesson uses nonconstant targets.

## Your Tasks

1. Implement `relative_fit(actual, predicted)` to return R-squared without clipping negative values.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
