---
title: 'Exercise: Stack sky snapshots'
slug: exercise-three-dimensional-stack
order: 8
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Convert multiple sky-grid snapshots to a three-dimensional array.
seo_title: 'Exercise: Stack sky snapshots | NumPy for beginners'
seo_description: Convert multiple sky-grid snapshots to a three-dimensional array.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise three dimensional stack
---

Sky snapshots arrive as nested lists: frames contain rows, and rows contain pixel values. Unlike the fixed scoreboard, your function must accept different numbers of frames and rows.

The starter's `sky_stack` returns `None`. Edit `main.py`, press **Run** to see the snapshot array, then **Submit** to check other grid sizes.

## Your Tasks

1. Make `sky_stack(snapshots)` return a three-dimensional array of the supplied grids.
