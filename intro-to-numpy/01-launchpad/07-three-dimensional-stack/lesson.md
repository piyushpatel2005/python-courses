---
title: Stack observation frames
slug: three-dimensional-stack
order: 7
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Create a three-dimensional array of frames, rows, and columns.
seo_title: Stack observation frames | NumPy for beginners
seo_description: Create a three-dimensional array of frames, rows, and columns.
seo_keywords:
  - NumPy
  - Python arrays
  - three dimensional stack
---

The scoreboard now stores snapshots over time. An outer list groups frames; each frame contains rows; each row contains columns. For two frames of one row and two columns, `shape` is `(2, 1, 2)`.

Edit the array literal in `main.py`, press **Run** to see the frame count change from 2 to 3, then **Submit**.

## Your Task

1. Add the scoreboard frame `[[9, 8], [7, 6]]` as a third nested list inside `np.array`.
