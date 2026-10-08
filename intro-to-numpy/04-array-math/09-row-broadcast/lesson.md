---
title: Add an offset to each grid row
slug: row-broadcast
order: 9
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: 'A grid with shape `(2, 3)` and vector of shape `(3,)` align from the right:
  the vector is reused across each row without constructing a tiled copy.'
seo_title: Add an offset to each grid row | NumPy
seo_description: 'A grid with shape `(2, 3)` and vector of shape `(3,)` align from
  the right: the vector is reused across each row without constructing a tiled copy.
  Practice NumPy in the browser.'
seo_keywords:
  - NumPy
  - Python
  - row broadcast
hints:
  - The vector length must match the grid’s final dimension.
---

A sky grid has a different correction for each column.

A grid with shape `(2, 3)` and vector of shape `(3,)` align from the right: the vector is reused across each row without constructing a tiled copy.

![A three-element vector is reused across two rows of a grid](broadcast-row-offsets.svg)

## Your Task

1. Change `+` to `-`; Run and check that the three offsets act on both rows.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
