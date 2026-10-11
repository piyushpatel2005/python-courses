---
title: 'Exercise: correct a horizon map'
slug: exercise-row-broadcast
order: 10
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Subtract per-column background levels from a horizon map."
seo_title: 'Exercise: correct a horizon map | NumPy'
seo_description: "Subtract per-column background levels from a horizon map."
seo_keywords:
  - NumPy
  - Python
  - row broadcast
hints:
  - 'Subtract the 1D offsets directly; NumPy reuses them on each row.'
---

A horizon map has a background level for each column, shared by every row. Subtract those levels to reveal the corrected readings.

`offsets` is a 1D array whose length matches `grid.shape[1]`. Its first value applies to the first column in every row, not to the first row alone.

## Your Task

1. In `remove_background`, return `grid - offsets` using broadcasting.

Run `main.py` to check the rows `[10 20]` and `[12 24]`, then Submit.
