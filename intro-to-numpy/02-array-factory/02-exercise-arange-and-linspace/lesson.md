---
title: 'Exercise: Schedule sensor samples'
slug: exercise-arange-and-linspace
order: 2
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Produce stepped sample times and endpoint-inclusive calibration positions.
seo_title: 'Exercise: Schedule sensor samples | NumPy for beginners'
seo_description: Produce stepped sample times and endpoint-inclusive calibration positions.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise arange and linspace
---

The station needs two kinds of schedule: stepped sample times with an excluded stop, and evenly spaced calibration marks with included endpoints. Use the two constructors from the preceding demo on new inputs. The sample times use integer steps; calibration counts will be at least two.

Both starter functions return `None`. Edit `main.py`, press **Run** to see both schedules, then **Submit** to check other starts, stops, and counts.

## Your Tasks

1. Make `sample_times(start, stop, step)` return `np.arange` values; the stop is excluded.
2. Make `calibration_marks(start, stop, count)` return `np.linspace` values including both endpoints.
