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

The station now sends several rows at once. Each row contains the same number of readings, but different stations can have different grid sizes.

Use the incoming `rows` value rather than rebuilding the sample grid. NumPy will preserve the nesting when it creates the array.

## Your Tasks

1. Make `station_grid(rows)` return a NumPy array of the supplied nested rows.

Replace `return None` in `main.py`, then Run. The sample should display two rows: `5 6` and `7 8`. Submit also checks a wider grid.

For this exercise, the input is already rectangular. You don't need to add checks for uneven row lengths.
