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

The arcade timer needs regular ticks. `arange(start, stop, step)` chooses a step and excludes the stop; `linspace(start, stop, count)` chooses how many equally spaced points to put between two included endpoints.

Edit `main.py`, press **Run** to see tick 8 join the countdown while the calibration points stay the same, then **Submit**.

## Your Task

1. Change the tick `arange` stop from 8 to 10; leave the `linspace` alone.
