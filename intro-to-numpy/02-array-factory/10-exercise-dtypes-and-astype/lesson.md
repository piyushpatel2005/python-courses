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

The same readings can be useful as on/off flags, text labels, or complex values. Each conversion makes a separate array; changing it will not change the original readings.

The starter creates `values` from the supplied readings and returns three unfinished slots. Use `values.astype(...)` for each conversion. Boolean conversion maps zero to `False` and every nonzero value to `True`; conversion to complex adds an imaginary part of zero.

## Your Tasks

1. Set `flags` to the Boolean conversion of `values`.
2. Set `labels` to the string conversion of `values`.
3. Set `complex_values` to the complex conversion of `values`.

Edit `main.py`, press **Run** to inspect the arrays, then **Submit** to check each conversion on other readings.

You can now generate arrays and choose their element types. After the quiz, you will select individual readings and smaller regions from these arrays.
