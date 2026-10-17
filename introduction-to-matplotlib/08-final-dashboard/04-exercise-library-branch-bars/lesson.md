---
title: 'Exercise: Aggregate branch visits'
slug: exercise-library-branch-bars
order: 4
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Clean incomplete library records and plot branch totals.'
seo_title: 'Exercise: Aggregate branch visits | Introduction to Matplotlib'
seo_description: 'Clean incomplete library records and plot branch totals.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'exercise'
  - 'aggregate'
  - 'branch'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Exercise: Aggregate branch visits

The next library export has some missing branch names or visit counts. Rows missing either cannot contribute to a named branch total. Group the remaining records, sort branches by name, and draw proportional bars. Return the grouped Series so its values can also be used in a report.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Return a branch-indexed, alphabetically sorted Series of summed visits from `library_totals(frame)` after dropping rows missing `branch` or `visits`.
2. Plot one bar per branch in `library_bars(frame)` with `Visits` units and a zero baseline.
