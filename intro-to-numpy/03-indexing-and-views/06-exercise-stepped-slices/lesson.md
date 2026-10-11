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
seo_description: Replace alternating interior readings while preserving both endpoints and the input array.
seo_keywords:
  - NumPy
  - Python
  - stepped slices
hints:
  - The stop `-1` excludes the final item; step `2` skips one item each time.
---

A station flags every other interior sample for recalibration.

Keep the first and last readings unchanged. As a slice stop, `-1` means the final position, which is excluded: `1:-1:2` therefore selects alternating interior readings even when the array length changes.

The starter uses `.copy()` to keep the input unchanged; the later views-and-copies lesson explores why this matters. Here you only need to fill selected slots in `updated`; the return line is already supplied.

## Your Tasks

1. Use a stepped slice assignment on `updated` to replace indices `1, 3, ...` strictly before the last item with `-9`.

Edit `main.py` and press **Run** to see which readings changed. **Submit** checks both odd and even array lengths.
