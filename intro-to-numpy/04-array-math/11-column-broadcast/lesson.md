---
title: Give each grid row its own baseline
slug: column-broadcast
order: 11
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A 1D vector of shape `(3,)` aligns with columns, not rows.
seo_title: Give each grid row its own baseline | NumPy
seo_description: A 1D vector of shape `(3,)` aligns with columns, not rows. Practice
  NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - column broadcast
hints:
  - A `(rows, 1)` column expands across columns; wrap only the attempted operation in
    `try`.
---

A grid needs a distinct correction for each row instead.

A 1D vector of shape `(3,)` aligns with columns, not rows. Turn row baselines into a `(3, 1)` column using `baselines[:, np.newaxis]`. Dimensions match if equal or one is `1`; otherwise arithmetic raises `ValueError`.

## Your Task

1. Change `+` to `-`; Run shows the `(3, 1)` shape and the handled incompatible-shape error.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
