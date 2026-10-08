---
title: 'Exercise: mute alternating samples'
slug: exercise-stepped-slices
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A station flags every other interior sample for recalibration.
seo_title: 'Exercise: mute alternating samples | NumPy'
seo_description: A station flags every other interior sample for recalibration. Practice
  NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - stepped slices
hints:
  - The stop `-1` excludes the final item; step `2` skips one item each time.
---

A station flags every other interior sample for recalibration.

Use the preceding editable example as a pattern, but solve this new data task in `main.py`.

The starter uses `.copy()` to keep the input unchanged; the later views-and-copies lesson explores why this matters. Here you only need to fill selected slots in `updated`.

## Your Tasks

1. Use a stepped slice assignment on `updated` to replace indices `1, 3, ...` strictly before the last item with `-9`, then return it.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.
