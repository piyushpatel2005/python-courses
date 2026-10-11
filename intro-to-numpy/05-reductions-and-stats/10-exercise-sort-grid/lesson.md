---
title: "Order each observation"
slug: exercise-sort-grid
order: 10
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Return a sorted copy of each night’s observations."
seo_title: "Order each observation | Intro to NumPy"
seo_description: "Return a sorted copy of each night’s observations."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'Use `np.sort`, which returns a copy, rather than the in-place `.sort()` method.'
---

Each row holds one night's observations. Keep nights separate while arranging each row from lowest to highest. The original grid must remain available in arrival order.

## Your Task

1. In `ordered_nights`, return a sorted copy of each row using `np.sort(grid, axis=1)`.

Run `main.py` to check `[2 5 7]` and `[1 6 9]`, then Submit. Here axis 1 means sorting across columns within each row, not sorting down a column.
