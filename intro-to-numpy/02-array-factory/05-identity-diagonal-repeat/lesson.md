---
title: Build patterns without loops
slug: identity-diagonal-repeat
order: 5
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Create identity grids, custom diagonals, and repeated values.
seo_title: Build patterns without loops | NumPy for beginners
seo_description: Create identity grids, custom diagonals, and repeated values.
seo_keywords:
  - NumPy
  - Python arrays
  - identity diagonal repeat
---

The sound board needs three patterns without hand-writing every cell. `np.eye(n)` places ones on the main diagonal of an `n` by `n` grid; `np.diag(weights)` places chosen values there and zeros elsewhere. `np.repeat(value, times)` makes a flat run of values.

Edit `main.py`, press **Run** to see the identity cue grow from `(3, 3)` to `(4, 4)` while the other patterns stay the same, then **Submit**.

## Your Task

1. Change the identity cue from 3 channels to 4.
