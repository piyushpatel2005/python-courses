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

The sky camera also sends frames, but its grids can have different dimensions from the scoreboard's grids. Your function should preserve the structure it receives.

Within one input stack, every frame has the same shape. The sample contains two frames of one row and two columns: `(2, 1, 2)`.

## Your Tasks

1. Make `sky_stack(snapshots)` return a NumPy array of the supplied frames.

Replace `return None` in `main.py`. Run to see the two frames, separated by an extra pair of brackets in the output. Submit checks their values and another stack size. No extra frame needs to be added here.
