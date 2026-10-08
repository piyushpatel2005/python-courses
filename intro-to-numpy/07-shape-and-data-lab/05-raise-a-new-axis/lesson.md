---
title: Raise a new axis
slug: raise-a-new-axis
order: 5
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Turn a reading vector into a column with np.newaxis.
seo_title: Raise a new axis | Intro to NumPy
seo_description: Turn a reading vector into a column with np.newaxis.
seo_keywords:
  - numpy
  - array shape
  - raise a new axis
hints:
  - Read the shape of each intermediate array before editing another line.
---

# Raise a new axis

A calibration value belongs beside each sensor row. A one-dimensional array with shape `(3,)` has no row/column orientation. `values[:, np.newaxis]` inserts a length-one column axis, producing `(3, 1)`. By contrast, `values[np.newaxis, :]` makes `(1, 3)`.

In `main.py`, change **only** the indexing expression to `values[:, np.newaxis]`. Run to compare the shape, then Submit. The readings themselves do not multiply.

## Your Tasks

1. Insert `np.newaxis` after the slice to make a three-row column.
