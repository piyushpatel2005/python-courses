---
title: 'Exercise: trace a grid column'
slug: exercise-grid-coordinates
order: 4
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: An observation grid needs its middle column and the reading at the bottom-right
  corner.
seo_title: 'Exercise: trace a grid column | NumPy'
seo_description: Select a grid column and its bottom-right cell with independent checks for each result.
seo_keywords:
  - NumPy
  - Python
  - grid coordinates
hints:
  - A colon keeps every row; `-1` chooses the final row or column.
---

Find two parts of a new observation grid: its second column and its bottom-right reading. The supplied grids always have three columns, so column `1` is the middle column. The number of rows may change.

The starter returns `(column, corner)`. Replace each `None` with a selection from `grid`; the tuple can still print while one slot is unfinished. A colon keeps all rows, and `-1` means the final position on either axis.

## Your Tasks

1. Set `column` to column index `1` using two-dimensional indexing.
2. Set `corner` to the bottom-right cell using two-dimensional indexing.

Edit `main.py`, press **Run** to inspect the pair, then **Submit** to check each selection.
