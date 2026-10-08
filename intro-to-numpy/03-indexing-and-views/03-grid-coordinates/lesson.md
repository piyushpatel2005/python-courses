---
title: Read a sky grid
slug: grid-coordinates
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: For a 2D array, `grid[row, column]` picks one cell; `grid[row, :]` selects
  a whole row, while `grid[:, column]` selects a column.
seo_title: Read a sky grid | NumPy
seo_description: For a 2D array, `grid[row, column]` picks one cell; `grid[row, :]`
  selects a whole row, while `grid[:, column]` selects a column. Practice NumPy in
  the browser.
seo_keywords:
  - NumPy
  - Python
  - grid coordinates
hints:
  - A colon keeps every row; `-1` chooses the final row or column.
---

A camera stores a tiny sky map as rows and columns.

For a 2D array, `grid[row, column]` picks one cell; `grid[row, :]` selects a whole row, while `grid[:, column]` selects a column.

## Your Task

1. Change the row index to `1`, then Run should print `7` for the cell (followed by the middle column).

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
