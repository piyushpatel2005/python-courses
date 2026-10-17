---
title: 'Exercise: Compare library branches'
slug: exercise-honest-library-bars
order: 2
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Build a branch comparison whose bar lengths start at zero.'
seo_title: 'Exercise: Compare library branches | Introduction to Matplotlib'
seo_description: 'Build a branch comparison whose bar lengths start at zero.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'exercise'
  - 'compare'
  - 'library'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Exercise: Compare library branches

A library report compares branch visits. Transfer the zero-baseline pattern from the garden chart, but take the branch names and counts from any supplied DataFrame. Keep the units clear so a reader knows these are visits, not percentages.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Plot one bar per row from `frame["branch"]` and `frame["visits"]` on `ax`.
2. Label the y-axis `Visits` and set its lower limit to zero.
