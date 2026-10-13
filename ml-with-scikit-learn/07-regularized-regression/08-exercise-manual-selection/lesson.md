---
title: 'Exercise: select settings on validation data'
slug: exercise-manual-selection
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: Compare a supplied small degree/alpha candidate list using validation MAE
  and freeze a choice.
seo_title: 'Exercise: select settings on validation data | Scikit-Learn'
seo_description: Compare a supplied small degree/alpha candidate list using validation
  MAE and freeze a choice with a different practice fixture.
seo_keywords:
  - scikit-learn
  - manual selection
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
---

The new synthetic target has both a slope and curvature, and the candidate alpha values differ. Keep the provided order when recording errors; callers need to know which number belongs to which pair.

The supplied list has only three candidates. Trying many alternatives against a tiny validation set can adapt to its noise, so do not treat a small winning margin as strong evidence. Once a choice is frozen, a later stage may refit it on development rows and report final test error. It must not return to this loop after seeing test results.

## Your Tasks

1. Implement `select_settings` to fit each supplied `(degree, alpha)` pipeline on training only and return `(winning_pair, errors)` in candidate order. Minimize validation MAE and resolve exact ties by first occurrence.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
