---
title: "Find the loudest reading"
slug: find-extremes
order: 1
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Distinguish a maximum reading from its zero-based position."
seo_title: "Find the loudest reading | Intro to NumPy"
seo_description: "Distinguish a maximum reading from its zero-based position."
seo_keywords: [numpy, arrays, statistics]
hints:
  - '`max` gives a reading; `argmax` gives its zero-based position.'
---

You can now correct a whole array. A **reduction** goes the other way: it turns several readings into a summary value.

An arcade sound meter recorded `[42, 68, 51]`. `np.sum(readings)` adds all three values, `np.min(readings)` finds the smallest, and `np.max(readings)` finds the largest.

`np.argmin(readings)` and `np.argmax(readings)` return zero-based positions instead of values. Here the maximum is 68 at position 1. If an extreme occurs more than once, its first position wins. We use one-dimensional arrays for these position checks.

## Your Task

1. Change `np.min` to `np.max` in `loudest`.

Edit `main.py`, Run to see `68`, then Submit.
