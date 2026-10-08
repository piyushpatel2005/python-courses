---
title: 'Exercise: Decode a sensor feed'
slug: exercise-import-and-convert
order: 4
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Write a reusable conversion function for incoming sensor lists.
seo_title: 'Exercise: Decode a sensor feed | NumPy for beginners'
seo_description: Write a reusable conversion function for incoming sensor lists.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise import and convert
---

Now apply the pattern to a fresh station feed. `np.array(values)` makes a new `ndarray`; the original list remains a list. The sample call at the bottom of `main.py` prints your function's result.

The starter returns `None` so it runs, but Submit will fail until you complete `make_feed`. Edit `main.py`, press **Run** for a quick check, then **Submit**.

## Your Tasks

1. Make `make_feed(values)` return a NumPy array containing the supplied list values.
