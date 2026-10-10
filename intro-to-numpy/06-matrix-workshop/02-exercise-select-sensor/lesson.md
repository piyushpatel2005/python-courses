---
title: "Select a sensor history"
slug: exercise-select-sensor
order: 2
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: 'Write a reusable function that selects one sensor across every night.'
seo_title: "Select a sensor history | Intro to NumPy"
seo_description: 'Write a reusable function that selects one sensor across every night.'
seo_keywords: [numpy, arrays, matrices]
hints:
  - Put a colon in the row position and the parameter column in the column position.
---

The field team needs the same kind of history from a different panel. This time, write a function so they can choose a sensor instead of editing the slice each night.

The starter supplies `grid` and `column` as function parameters. Use those inputs rather than the sample values printed below the function. Return a one-dimensional array with one reading per row; do not rearrange the readings.

Edit `main.py` and Run. For the supplied panel, sensor `1` should give `[1 6 8]`. Submit also checks a different panel and column.

## Your Task

1. Implement `sensor_history(grid, column)` with 2D slicing to return all rows of the requested column.
