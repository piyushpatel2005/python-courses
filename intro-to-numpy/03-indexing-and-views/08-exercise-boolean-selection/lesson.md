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
seo_description: Mark signals below a supplied threshold without changing the input array or equal values.
seo_keywords:
  - NumPy
  - Python
  - boolean selection
hints:
  - Select with `cleaned[cleaned < threshold]` on the left side of `=`.
---

A different instrument must keep only signals at or above a threshold and mark weak ones.

Here “weak” means strictly below `threshold`; a value equal to the threshold stays unchanged. The supplied `.copy()` keeps the input array safe. Add your mask assignment to `cleaned` before the existing return line. Try a threshold equal to one of the sample values to check that boundary.

## Your Tasks

1. Build a boolean mask on `cleaned` using the supplied `threshold` and assign `-1` to every weak signal.

Edit `main.py` and press **Run** to inspect the cleaned signals. **Submit** checks another threshold and confirms that the original array stays unchanged.
