---
title: 'Exercise: Compare routes without color alone'
slug: exercise-accessible-route-lines
order: 10
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Add labeled line styles and a legend to a two-route chart.'
seo_title: 'Exercise: Compare routes without color alone | Introduction to Matplotlib'
seo_description: 'Add labeled line styles and a legend to a two-route chart.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'exercise'
  - 'compare'
  - 'routes'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Exercise: Compare routes without color alone

Now the routes arrive as columns rather than lists. Plot both, giving each route a name, a distinct marker, and a distinct line style. The reader should still be able to identify routes if the colors disappear.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Plot both route columns against `day` with labels `East route` and `West route`.
2. Give the lines different markers and line styles, and display a legend.
