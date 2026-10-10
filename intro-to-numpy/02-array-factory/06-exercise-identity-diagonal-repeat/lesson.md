---
title: 'Exercise: Wire a sensor pattern'
slug: exercise-identity-diagonal-repeat
order: 6
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Create identity, weighted diagonal, and repeated sensor calibration arrays.
seo_title: 'Exercise: Wire a sensor pattern | NumPy for beginners'
seo_description: Create identity, weighted diagonal, and repeated sensor calibration
  arrays.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise identity diagonal repeat
---

Build three calibration patterns using the constructors you just tried. An identity grid has ones on its main diagonal and zeros elsewhere. A weighted diagonal uses the supplied weights instead of ones. A repeated signal is a one-dimensional array containing the same value several times.

Each starter function returns `None`. Replace those returns one at a time, using the function arguments so your code works beyond the printed examples.

## Your Tasks

1. Make `station_identity(count)` return an identity grid using `np.eye`.
2. Make `station_weights(weights)` return a grid with the supplied weights on its main diagonal using `np.diag`.
3. Make `hold_signal(value, times)` return the value repeated `times` times using `np.repeat`.

Edit `main.py`, press **Run** to inspect the three patterns, then **Submit** to check other sizes and values.
