---
title: 'Exercise: Map station rows'
slug: exercise-two-dimensional-grid
order: 6
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Convert nested station readings to a rectangular two-dimensional array.
seo_title: 'Exercise: Map station rows | NumPy for beginners'
seo_description: Convert nested station readings to a rectangular two-dimensional
  array.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise two dimensional grid
---

The station sends nested rows instead of the sound board's fixed grid. Convert any rectangular set of rows to an array: the result's shape should be `(rows, columns)`.

The starter's `station_grid` returns `None`. Edit `main.py`, press **Run** to see a grid instead of `None`, then **Submit** to check other row sizes.

## Your Tasks

1. Make `station_grid(rows)` convert nested station rows into a NumPy array.
