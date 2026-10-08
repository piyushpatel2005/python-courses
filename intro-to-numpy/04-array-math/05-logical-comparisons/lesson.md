---
title: Find a usable band
slug: logical-comparisons
order: 5
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: Comparisons return arrays of booleans.
seo_title: Find a usable band | NumPy
seo_description: Comparisons return arrays of booleans. Practice NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - logical comparisons
hints:
  - Put each comparison in parentheses and join them with `&`.
---

A detector accepts values within a range.

Comparisons return arrays of booleans. Combine array conditions with `&` (and), `|` (or), and parentheses—not Python `and`/`or`. `np.array_equal(a, b)` yields one boolean for whole-array equality.

## Your Task

1. Change the upper bound to `10`, Run and inspect both the mask and its whole-array check.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
