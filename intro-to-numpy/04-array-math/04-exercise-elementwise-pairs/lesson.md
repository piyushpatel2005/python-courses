---
title: 'Exercise: find sensor agreement'
slug: exercise-elementwise-pairs
order: 4
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A pair of rooftop sensors needs a per-reading difference, not one total.
seo_title: 'Exercise: find sensor agreement | NumPy'
seo_description: A pair of rooftop sensors needs a per-reading difference, not one
  total. Practice NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - elementwise pairs
hints:
  - Do not use `sum`; subtract the arrays directly.
---

A pair of rooftop sensors needs a per-reading difference, not one total.

Use the preceding editable example as a pattern, but solve this new data task in `main.py`.

## Your Tasks

1. Return `primary - reference` as a NumPy array with one difference per reading.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.
