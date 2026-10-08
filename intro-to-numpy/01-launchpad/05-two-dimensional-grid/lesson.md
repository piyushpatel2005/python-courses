---
title: Build a two-dimensional grid
slug: two-dimensional-grid
order: 5
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Represent rows of observations as a rectangular two-dimensional array.
seo_title: Build a two-dimensional grid | NumPy for beginners
seo_description: Represent rows of observations as a rectangular two-dimensional array.
seo_keywords:
  - NumPy
  - Python arrays
  - two dimensional grid
---

The sound board records levels in rows. Each inner list is one row; for a rectangular grid, `shape` reports `(rows, columns)`. The diagram below shows which direction each count describes.

In `main.py`, add one row to the arcade sound board. Press **Run** and watch its shape change from `(2, 2)` to `(3, 2)`, then **Submit**.

Here is a separate example: two rows of three readings have shape `(2, 3)`. The diagram labels **indices** starting at 0, but `shape` reports the **counts** of rows and columns.

![Two rows and three columns in a grid, with shape (2, 3)](array-rows-columns-shape.svg)

## Your Task

1. Add `[7, 8]` as the sound board’s third row.
