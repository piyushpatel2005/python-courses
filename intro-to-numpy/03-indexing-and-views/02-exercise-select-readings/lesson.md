---
title: 'Exercise: choose a signal pair'
slug: exercise-select-readings
order: 2
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A different receiver wants its last reading first, followed by its second
  reading.
seo_title: 'Exercise: choose a signal pair | NumPy'
seo_description: Return the last and second readings from arrays of different lengths using an index list.
seo_keywords:
  - NumPy
  - Python
  - select readings
hints:
  - Use `-1` for the final item and `1` for the second.
---

A different receiver wants its last reading first, followed by its second reading.

The `readings` argument is already a one-dimensional NumPy array with at least two items. Use `-1` for its last item even when its length changes; do not type the example values into your answer.

## Your Tasks

1. Make `choose_pair(readings)` use a list of indices to return an array containing the last reading, then the second reading.

Edit `main.py` and press **Run** to see the requested pair. **Submit** checks that your indices also work on a longer array.
