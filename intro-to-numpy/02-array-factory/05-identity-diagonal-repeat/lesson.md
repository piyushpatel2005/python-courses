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

The sound board needs three patterns without hand-writing every cell. `np.eye(n)` places ones on the main diagonal of an `n` by `n` grid; `np.diag(weights)` places chosen values there and zeros elsewhere. The main diagonal runs from top-left to bottom-right. `np.repeat(value, times)` makes a flat run of values.

For example, `np.diag([2, 5, 7])` builds `[[2, 0, 0], [0, 5, 0], [0, 0, 7]]`. In the supplied print statement, `gains.diagonal()` reads those diagonal values back, and `.tolist()` formats them as a Python list.

Edit `main.py`, press **Run** to see the identity cue grow from `(3, 3)` to `(4, 4)` while the other patterns stay the same, then **Submit**.

## Your Task

1. Change the argument in `np.eye(3)` to `4`.
