---
title: 'Exercise: censor weak signals'
slug: exercise-boolean-selection
order: 8
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A different instrument must keep only signals at or above a threshold and
  mark weak ones.
seo_title: 'Exercise: censor weak signals | NumPy'
seo_description: A different instrument must keep only signals at or above a threshold
  and mark weak ones. Practice NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - boolean selection
hints:
  - Select with `cleaned[cleaned < threshold]` on the left side of `=`.
---

A different instrument must keep only signals at or above a threshold and mark weak ones.

Use the preceding editable example as a pattern, but solve this new data task in `main.py`.

## Your Tasks

1. Build a boolean mask on `cleaned` using the supplied `threshold` and assign `-1` to every weak signal.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.
