---
title: Fold a signal
slug: fold-a-signal
order: 1
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Reshape a flat signal into rows without changing its size.
seo_title: Fold a signal | Intro to NumPy
seo_description: Reshape a flat signal into rows without changing its size.
seo_keywords:
  - numpy
  - array shape
  - fold a signal
hints:
  - Read the shape of each intermediate array before editing another line.
---

# Fold a signal

The Pocket Observatory receives six light readings in a single strip. The starter folds them into two rows; you will change it to three rows. `reshape` changes the dimensions, not the number of readings: the product of the dimensions must equal `size`. `ravel()` reads the rows back into a flat sequence in row-major order by default.

![A six-reading strip folds into a two-by-three grid, then unrolls into a six-reading strip](signal-shape-fold.svg)

Edit the **one** shape argument in `main.py` from `(2, 3)` to `(3, 2)`. Press Run: the displayed shape should become `(3, 2)` and its size stay 6. Then Submit. A `(4, 2)` shape would fail because eight slots cannot hold six values.

## Your Tasks

1. Change the `reshape` dimensions to `(3, 2)`; keep all six readings.
