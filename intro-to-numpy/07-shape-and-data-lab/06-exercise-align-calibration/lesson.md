---
title: 'Exercise: align calibration'
slug: exercise-align-calibration
order: 6
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Prepare row and column inputs by adding an axis of length one.
seo_title: 'Exercise: align calibration | Intro to NumPy'
seo_description: Prepare row and column inputs by adding an axis of length one.
seo_keywords:
  - numpy
  - array shape
  - exercise align calibration
hints:
  - Check that the inserted dimension is 1, while the other dimension keeps the input length.
---

# Exercise: align calibration

A second sensor has four row offsets, while a timer supplies three time offsets. Prepare the shapes separately before combining them: row offsets need a column, and time offsets need a row.

Use `np.newaxis` rather than duplicating the readings. The sample shapes should be `(4, 1)` and `(1, 3)`. These shapes can broadcast together to make a four-by-three comparison, but this exercise only asks you to prepare the two inputs.

Edit the helpers in `main.py`. Run after each change to check its printed shape, then Submit. The checks also try shorter arrays.

## Your Tasks

1. Implement `as_column(offsets)` with `np.newaxis` to return a column containing the offsets.
2. Implement `as_row(ticks)` with `np.newaxis` to return one row containing the ticks.
