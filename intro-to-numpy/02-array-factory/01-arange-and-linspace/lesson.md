---
title: Mark ticks and intervals
slug: arange-and-linspace
order: 1
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Create stepped values with arange and inclusive evenly spaced points with
  linspace.
seo_title: Mark ticks and intervals | NumPy for beginners
seo_description: Create stepped values with arange and inclusive evenly spaced points
  with linspace.
seo_keywords:
  - NumPy
  - Python arrays
  - arange and linspace
---

You have built arrays from lists and checked their shapes. When values follow a regular pattern, a constructor can generate them for you.

`np.arange(start, stop, step)` works much like Python's `range`: it uses the chosen step and leaves out the stop. Here, `np.arange(2, 8, 2)` gives ticks `[2, 4, 6]`.

`np.linspace(start, stop, count)` instead chooses how many equally spaced points to make. With a count of at least two, it includes both endpoints by default: `np.linspace(0, 1, 3)` gives `[0.0, 0.5, 1.0]`. Use this when the number of points matters. For decimal steps, prefer `linspace` rather than relying on `arange` to hit a floating-point endpoint.

The supplied `.tolist()` calls make the arrays print as Python lists. Leave `points` unchanged for this small edit.

## Your Task

1. Change the stop in the `ticks` call from `8` to `10`.

Edit `main.py`, press **Run** to see tick `8` added, then **Submit**. Next you will build both kinds of sequence inside functions.
