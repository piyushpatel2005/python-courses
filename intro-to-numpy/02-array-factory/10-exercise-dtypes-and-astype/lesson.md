---
title: 'Exercise: Label observation types'
slug: exercise-dtypes-and-astype
order: 10
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Convert station readings into Boolean flags, text labels, and complex values.
seo_title: 'Exercise: Label observation types | NumPy for beginners'
seo_description: Convert station readings into Boolean flags, text labels, and complex
  values.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise dtypes and astype
---

The station needs three views of the same readings: on/off flags, text labels, and complex values. Convert one numeric array with `astype(bool)`, `astype(str)`, and `astype(complex)`; each call returns a new array. Their `dtype.kind` values are `b`, `U`, and `c` respectively.

The starter's `typed_feeds` returns `None`. Edit `main.py`, press **Run** to inspect the three arrays, then **Submit** to check other readings.

## Your Tasks

1. Make `typed_feeds(readings)` first create a NumPy array, then return its Boolean, string, and complex conversions in that order using `astype`.

The toolkit can now build grids, replay test observations, and label their values. Take the module quiz to check which constructor fits a new feed.
