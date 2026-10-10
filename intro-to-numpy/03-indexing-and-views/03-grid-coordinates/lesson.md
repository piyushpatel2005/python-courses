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
seo_description: Use row and column coordinates to select one cell or a whole column from a NumPy grid.
seo_keywords:
  - NumPy
  - Python
  - grid coordinates
hints:
  - In `grid[row, column]`, change the number before the comma.
---

A camera stores a tiny sky map as rows and columns.

Both coordinates start at zero. In `grid[row, column]`, the position before the comma chooses the row, and the position after it chooses the column. A colon means “keep everything” in that position: `grid[row, :]` selects a whole row, while `grid[:, column]` selects a whole column.

Here, row `1` is the second row, `[4, 7, 9]`. Column `1` contains `[3, 7]`, across both rows.

![Row and column coordinates for the exact sky grid, highlighting cell 7 and column 1](grid-row-column-selection.svg)

## Your Task

1. Change the row index in `spot` to `1`, keeping the column at `1`.

Edit `main.py` and press **Run**. The cell should print as `7`, followed by the middle column `[3 7]`. Then **Submit** to check the new coordinates.
