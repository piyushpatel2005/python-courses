---
title: "Sort within rows"
slug: sort-a-grid
order: 9
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Sort within rows with NumPy arrays."
seo_title: "Sort within rows | Intro to NumPy"
seo_description: "Practice sort within rows in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, statistics]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

A grid of sound samples has one row per microphone. `np.sort(grid, axis=1)` sorts within each row; `axis=0` sorts down each column. The result is a new array. The default for a 2D `np.sort(grid)` is the last axis (`axis=-1`, here axis 1). Sorting along axis 0 instead ranks each column independently.

Run `main.py` first, make the small edit, then Submit.

## Your Task

1. Change the axis to `1` to sort each microphone’s readings independently.
