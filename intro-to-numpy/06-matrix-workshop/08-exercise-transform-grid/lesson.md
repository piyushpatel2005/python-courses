---
title: "Transform a whole panel"
slug: exercise-transform-grid
order: 8
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Transform a whole panel with NumPy arrays."
seo_title: "Transform a whole panel | Intro to NumPy"
seo_description: "Practice transform a whole panel in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, matrices]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

Each night is a row with three sensor values. A calibration matrix maps those three channels into two derived channels. 

Type the technique in `main.py`, press Run to inspect the result, then Submit.

## Your Task

1. Implement `transform_panel(grid, calibration)` with matrix multiplication (not elementwise `*`).
