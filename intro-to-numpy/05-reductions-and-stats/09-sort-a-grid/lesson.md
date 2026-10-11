---
title: "Sort within rows"
slug: sort-a-grid
order: 9
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Sort each microphone’s readings without changing the original grid."
seo_title: "Sort within rows | Intro to NumPy"
seo_description: "Sort each microphone’s readings without changing the original grid."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'Sorting on axis 1 stays within each row and keeps the grid shape.'
---

A grid of sound samples has one row per microphone. Sorting helps inspect its low and high values, but changes their order: keep the original if you need to know when each reading occurred.

`np.sort(samples, axis=1)` sorts across columns within each row. `axis=0` sorts down each column independently. Unlike a reduction, sorting keeps both dimensions and the same shape. It returns a new array; the input stays unchanged.

The default axis is the last one (`axis=-1`), which is axis 1 for this 2D grid. We write the axis explicitly here to make the direction clear.

## Your Task

1. Change the axis in `by_microphone` from `0` to `1`.

Run `main.py`: the sorted rows should be `[3 6 8]` and `[1 4 9]`. Then Submit.
