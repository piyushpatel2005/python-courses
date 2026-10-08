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

Make three station patterns for arbitrary inputs: an identity grid, a weighted diagonal grid, and a flat repeated signal. These transfer the sound board's patterns to new sizes and values.

Each starter function returns `None`. Edit `main.py`, press **Run** to see all three patterns, then **Submit** to check other sizes and values.

## Your Tasks

1. Make `station_identity(count)` return an identity grid using `np.eye`.
2. Make `station_weights(weights)` put the supplied weights on a diagonal using `np.diag`.
3. Make `hold_signal(value, times)` repeat one value with `np.repeat`.
