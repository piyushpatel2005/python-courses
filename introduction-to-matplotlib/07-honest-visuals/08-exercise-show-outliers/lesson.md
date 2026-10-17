---
title: 'Exercise: Keep outliers visible'
slug: exercise-show-outliers
order: 8
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Compare a full histogram with a zoom without dropping the long wait.'
seo_title: 'Exercise: Keep outliers visible | Introduction to Matplotlib'
seo_description: 'Compare a full histogram with a zoom without dropping the long wait.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'exercise'
  - 'keep'
  - 'outliers'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Exercise: Keep outliers visible

One bus arrived very late. A narrow histogram can hide it if the range cuts off at twenty minutes. Put the complete range alongside a close view; label the close view as a zoom and state how many observations it excludes. The function accepts any nonnegative wait times, so the disclosure must be computed rather than memorized.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Plot all waits in the left histogram with five bins; its counts must include the longest wait.
2. On the right plot only waits at or below `cutoff` with five bins, and title it `Detail ≤ {cutoff} min; {excluded} excluded`.
