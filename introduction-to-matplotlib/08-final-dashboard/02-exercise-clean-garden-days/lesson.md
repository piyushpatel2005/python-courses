---
title: 'Exercise: Clean garden readings'
slug: exercise-clean-garden-days
order: 2
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Drop missing readings and average repeated measurements by day.'
seo_title: 'Exercise: Clean garden readings | Introduction to Matplotlib'
seo_description: 'Drop missing readings and average repeated measurements by day.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'exercise'
  - 'clean'
  - 'garden'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Exercise: Clean garden readings

Garden sensors can report twice on a day, or leave a temperature missing. Remove missing temperatures before computing each day's mean; do not treat a blank as zero. `groupby('day')['temp_c'].mean()` gives a new series with one value per day. Plot it as a line in sorted day order. Using ISO dates makes the string order chronological.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Return a two-column DataFrame `day, temp_c` from `daily_garden(frame)`, sorted by day, with missing temperatures removed and repeated days averaged.
2. Plot the daily temperatures with a marked line and label the y-axis `Temperature (°C)`.
