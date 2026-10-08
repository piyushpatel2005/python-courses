---
title: 'Exercise: Label any observation'
slug: exercise-inspect-array-metadata
order: 10
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Report ndim, shape, size, and first-axis length for observation arrays.
seo_title: 'Exercise: Label any observation | NumPy for beginners'
seo_description: Report ndim, shape, size, and first-axis length for observation arrays.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise inspect array metadata
---

The observation labeler must work for both grids and stacks. Report `ndim` (axes), `shape` (length of each axis), `size` (all values), and `len` (first-axis length).

The starter's `describe_observation` returns `None`. Edit `main.py`, press **Run** to inspect its tuple for the sample grid, then **Submit** to check a stack too.

## Your Tasks

1. Make `describe_observation(observation)` return `(ndim, shape, size, len(observation))` in that order.
