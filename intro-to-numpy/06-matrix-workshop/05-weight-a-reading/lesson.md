---
title: "Weight a reading"
slug: weight-a-reading
order: 5
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Weight a reading with NumPy arrays."
seo_title: "Weight a reading | Intro to NumPy"
seo_description: "Practice weight a reading in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, matrices]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

A 1D dot product pairs readings and calibration weights, multiplies each pair, and sums. Unlike `*`, it returns one combined value. For these readings, the dot product is `2×3 + 4×1 + 6×2 = 22`. Elementwise `*` produces `[6, 4, 12]` instead.

Run `main.py` first, make the small edit, then Submit.

## Your Task

1. Change `*` to `np.dot(readings, weights)` to print the single weighted total 22.
