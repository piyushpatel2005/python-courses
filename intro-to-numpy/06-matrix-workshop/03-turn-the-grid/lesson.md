---
title: "Transpose a grid"
slug: turn-the-grid
order: 3
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Transpose a grid with NumPy arrays."
seo_title: "Transpose a grid | Intro to NumPy"
seo_description: "Practice transpose a grid in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, matrices]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

A display wants sensors down the page instead of nights. `.T` swaps rows and columns: shape `(2, 3)` becomes `(3, 2)` without changing the values. 

![A two-by-three observation grid turned into a three-by-two grid, with row and column roles exchanged](transpose-grid.svg)


Run `main.py` first, make the small edit, then Submit.

## Your Task

1. Replace `grid` with `grid.T` in the assignment and observe `(3, 2)`.
