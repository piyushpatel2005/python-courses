---
title: "Locate sensor extremes"
slug: exercise-sensor-extremes
order: 2
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Calculate a brightness total, its extremes, and their first positions."
seo_title: "Locate sensor extremes | Intro to NumPy"
seo_description: "Calculate a brightness total, its extremes, and their first positions."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'Fill the five named values in the return order; tied extrema use the first index.'
---

The Pocket Observatory stores brightness readings in arrival order. A total describes the whole series; minimum and maximum locate its range. Their indices tell you where those extremes occurred.

The starter supplies five named placeholders and returns them as a tuple. Replace one `None` at a time, keeping the return order and print call as supplied. Inputs are nonempty 1D arrays.

## Your Tasks

1. Set `total` to the sum of `readings` with `np.sum`.
2. Set `minimum` to the smallest reading with `np.min`.
3. Set `maximum` to the largest reading with `np.max`.
4. Set `min_index` to the first minimum's position with `np.argmin`.
5. Set `max_index` to the first maximum's position with `np.argmax`.

Run `main.py` after each edit, then Submit. For the supplied series, the minimum is 3 at index 1, and the maximum is 14 at index 2.
