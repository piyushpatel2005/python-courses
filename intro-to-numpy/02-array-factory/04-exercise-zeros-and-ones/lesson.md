---
title: 'Exercise: Prime observation panels'
slug: exercise-zeros-and-ones
order: 4
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Return blank and active station grids for any requested shape.
seo_title: 'Exercise: Prime observation panels | NumPy for beginners'
seo_description: Return blank and active station grids for any requested shape.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise zeros and ones
---

The station reserves panels of different sizes, one empty and one active. Pass `(rows, columns)` as a shape tuple to each constructor.

Both starter functions return `None`. Edit `main.py`, press **Run** to see both panels, then **Submit** to check other sizes.

## Your Tasks

1. Make `blank_panel(rows, columns)` return a NumPy grid of zeros.
2. Make `active_panel(rows, columns)` return a NumPy grid of ones.
