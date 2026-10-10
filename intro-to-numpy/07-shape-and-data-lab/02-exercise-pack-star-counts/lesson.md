---
title: 'Exercise: pack star counts'
slug: exercise-pack-star-counts
order: 2
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Unroll a count grid, then arrange its readings into four-column rows.
seo_title: 'Exercise: pack star counts | Intro to NumPy'
seo_description: Unroll a count grid, then arrange its readings into four-column rows.
seo_keywords:
  - numpy
  - array shape
  - exercise pack star counts
hints:
  - Use -1 for the unknown row count and 4 for the fixed column count.
---

# Exercise: pack star counts

Another station sends star counts in short rows, but its storage format needs four counts per row. Write two small helpers: one to unroll the incoming grid and another to pack a flat strip.

`grid.ravel()` returns the default row-by-row order. With `readings.reshape(-1, 4)`, the `-1` asks NumPy to work out the row count. Eight values need two rows; twelve need three. Only one dimension can be inferred, and the number of values must still be divisible by four.

Edit `main.py` and Run after each helper. The sample's flat line should become `[3 1 4 2]`; its packed version should have one row with four columns. Submit checks larger inputs as well. The two print calls are separate so you can finish one helper before the other.

## Your Tasks

1. Use `ravel()` in `unroll_counts(grid)` to return a one-dimensional array in row-major order.
2. Use `reshape(-1, 4)` in `pack_counts(readings)` to return rows of four readings.
