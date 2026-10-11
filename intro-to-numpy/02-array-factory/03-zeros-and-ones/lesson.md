---
title: Reserve blank and active grids
slug: zeros-and-ones
order: 3
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Create rectangular arrays initialized entirely to zeros or ones.
seo_title: Reserve blank and active grids | NumPy for beginners
seo_description: Create rectangular arrays initialized entirely to zeros or ones.
seo_keywords:
  - NumPy
  - Python arrays
  - zeros and ones
---

An arcade panel needs blank cells and lit cells. `np.zeros((rows, columns))` fills a grid with zeros; `np.ones((rows, columns))` fills one with ones. The inner parentheses hold the shape tuple `(rows, columns)`; the outer parentheses call the function. These constructors default to floating-point values; for whole-number cells, you can pass `dtype=int`. The later dtype lesson explains conversions.

The supplied `on.sum()` adds the lit cells, and `int(...)` prints that total as a whole number. You will use sums yourself in the statistics module.

Edit `main.py`, press **Run** to see the blank panel grow from `(2, 4)` to `(3, 4)` while the lit panel stays at eight cells, then **Submit**.

## Your Task

1. Set the shape in `blank` to `(3, 4)`.
