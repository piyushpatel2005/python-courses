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

Reserve two observation panels: one starts empty, with zeros in every cell; the other starts active, with ones. Their sizes come from the function arguments rather than fixed numbers.

Pass `(rows, columns)` as one shape tuple to the appropriate constructor. Each function starts by returning `None`, so you can finish and check one panel before working on the other.

## Your Tasks

1. Make `blank_panel(rows, columns)` return a NumPy grid of zeros with the requested shape.
2. Make `active_panel(rows, columns)` return a NumPy grid of ones with the requested shape.

Edit `main.py` and press **Run** to see the panels. **Submit** also checks different row and column counts.
