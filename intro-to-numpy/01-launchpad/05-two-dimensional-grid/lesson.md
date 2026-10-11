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

A sound board has rows of readings. To make a two-dimensional array, put one list per row inside an outer list:

```python
[[1, 2],
 [4, 5]]
```

Every row in this rectangular grid needs the same number of values. In `main.py`, `np.array(...)` converts those nested lists into an array. Its `shape` is `(2, 2)`: two rows, each with two columns.

The separate sky-grid example below has two rows and three columns. Notice the difference between an **index**, which starts at zero, and a **count**, which tells you how many items there are.

![A grid with row indexes 0 and 1, column indexes 0 through 2, and shape (2, 3)](array-rows-columns-shape.svg)

## Your Task

1. Add `[7, 8]` as the sound board's third row inside `np.array(...)`.

Keep the existing two rows. Run `main.py`: the shape should change from `(2, 2)` to `(3, 2)`. You added a row, but each row still has two columns. Submit to check the grid.
