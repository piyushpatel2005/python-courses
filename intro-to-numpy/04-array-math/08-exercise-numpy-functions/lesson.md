---
title: 'Exercise: transform a light curve'
slug: exercise-numpy-functions
order: 8
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Calculate sine values and natural logarithms as separate report results."
seo_title: 'Exercise: transform a light curve | NumPy'
seo_description: "Calculate sine values and natural logarithms as separate report results."
seo_keywords:
  - NumPy
  - Python
  - numpy functions
hints:
  - 'Replace each named placeholder without changing the supplied tuple return.'
---

A light-curve report needs two separate transformations: sine values for its angles and natural logarithms for its positive intensities.

The starter already returns a tuple in the right order. Replace one `None` at a time; leave the return line in place.

## Your Tasks

1. Set `sine_values` to `np.sin(angles)` inside `transform`.
2. Set `log_values` to `np.log(intensities)` inside `transform`.

Run `main.py` after each change. The sample eventually prints sine values near `[0.5 -1.]` and logarithms `[2. 3.]`. Submit to check each transformation.
