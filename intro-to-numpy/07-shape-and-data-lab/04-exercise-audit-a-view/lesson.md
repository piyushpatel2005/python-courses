---
title: 'Exercise: audit a view'
slug: exercise-audit-a-view
order: 4
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Compare row and column traversal, then inspect storage sharing.
seo_title: 'Exercise: audit a view | Intro to NumPy'
seo_description: Compare row and column traversal, then inspect storage sharing.
seo_keywords:
  - numpy
  - array shape
  - exercise audit a view
hints:
  - Read the shape of each intermediate array before editing another line.
---

# Exercise: audit a view

The camera grid needs two scan orders. `grid.ravel()` follows the rows, while `grid.T.ravel()` follows the columns. Neither order by itself proves that storage is shared. Test each produced array with `np.shares_memory` rather than assuming a transpose or reshape always copies or always shares.

In `main.py`, Run to compare orders and flags; Submit to check your functions with other rectangular grids.

## Your Tasks

1. Return the readings in column-first order with `column_scan(grid)`.
2. Return a pair of actual sharing flags `(row_shared, column_shared)` from `audit_scans(grid)` for `grid.ravel()` and `grid.T.ravel()`.
