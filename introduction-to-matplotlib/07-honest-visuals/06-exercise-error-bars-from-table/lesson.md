---
title: 'Exercise: Plot survey uncertainty'
slug: exercise-error-bars-from-table
order: 6
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Plot survey averages and supplied margins without inventing precision.'
seo_title: 'Exercise: Plot survey uncertainty | Introduction to Matplotlib'
seo_description: 'Plot survey averages and supplied margins without inventing precision.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'exercise'
  - 'plot'
  - 'survey'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Exercise: Plot survey uncertainty

The neighborhood library gathered a small survey. Its `margin` column gives the distance from each estimated score to either end of the reported interval. Use those given margins; do not divide them by the number of rows or silently substitute a standard deviation. Explain the measure in the y-axis label.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Draw an `errorbar` series from `day`, `score`, and `margin` with a visible marker and caps.
2. Label the y-axis `Survey score (points)` and the x-axis `Day`.
