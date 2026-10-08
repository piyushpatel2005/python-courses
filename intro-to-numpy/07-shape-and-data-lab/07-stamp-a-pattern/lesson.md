---
title: Stamp a pattern
slug: stamp-a-pattern
order: 7
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Distinguish element repeats from whole-pattern tiling.
seo_title: Stamp a pattern | Intro to NumPy
seo_description: Distinguish element repeats from whole-pattern tiling.
seo_keywords:
  - numpy
  - array shape
  - stamp a pattern
hints:
  - Read the shape of each intermediate array before editing another line.
---

# Stamp a pattern

The Pocket Observatory prints short exposure schedules. `np.repeat([2, 5], 2)` gives `[2, 2, 5, 5]`: each element is copied next to itself. `np.tile([2, 5], 2)` gives `[2, 5, 2, 5]`: the entire pattern is copied. Both grow the array; `np.newaxis` does not.

The starter repeats each value twice. Change **only** the count in `np.repeat` from `2` to `3`. Run to see three adjacent copies of each value; Submit to check the resulting array.

## Your Tasks

1. Repeat each exposure value three times. The supplied tiled comparison shows how the other operation differs.
