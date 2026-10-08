---
title: 'Exercise: flag an observation window'
slug: exercise-logical-comparisons
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A telescope must identify measurements inside caller-supplied lower and upper
  limits.
seo_title: 'Exercise: flag an observation window | NumPy'
seo_description: A telescope must identify measurements inside caller-supplied lower
  and upper limits. Practice NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - logical comparisons
hints:
  - Put each comparison in parentheses and join them with `&`.
---

A telescope must identify measurements inside caller-supplied lower and upper limits.

Use the preceding editable example as a pattern, but solve this new data task in `main.py`.

## Your Tasks

1. Return a boolean array selecting all readings between `low` and `high`, including both endpoints.
2. Make `matches_window(readings, expected, low, high)` return a single boolean: whether the mask from `in_window` exactly equals the expected boolean array, including its shape.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.
