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
  - Compare grid with each flattened scan, not just with the transpose.
---

# Exercise: audit a view

The camera offers two ways to scan a frame. `grid.ravel()` follows the rows. `grid.T.ravel()` first exchanges rows and columns, so its flat result follows the original columns. For the supplied camera, the column scan begins `2, 1, 5, 4`.

The order tells you which reading comes next; it does not tell you whether the result shares storage. Flattening a transposed grid can require a copy. Check each final scan against `grid` with `np.shares_memory` instead of deciding from its shape.

In `main.py`, the two scan arrays are already prepared inside `audit_scans`. Return their measured sharing flags in row-scan, column-scan order. Run to compare the values and flags, then Submit. A test uses a transposed input too, so fixed flags will not work.

## Your Tasks

1. Implement `column_scan(grid)` to return a flat array in column-first order.
2. Implement `audit_scans(grid)` to return the actual pair `(row_shared, column_shared)` for the two supplied scans.
