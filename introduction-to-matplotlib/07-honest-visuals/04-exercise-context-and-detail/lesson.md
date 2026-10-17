---
title: 'Exercise: Show context beside detail'
slug: exercise-context-and-detail
order: 4
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Pair full-range and zoomed line views of one temperature series.'
seo_title: 'Exercise: Show context beside detail | Introduction to Matplotlib'
seo_description: 'Pair full-range and zoomed line views of one temperature series.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'exercise'
  - 'show'
  - 'context'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Exercise: Show context beside detail

The detail view alone hides context. Give neighbors two panels with the *same* temperature readings: a full-range view on the left and an explicitly labeled detail view on the right. A zero baseline is a choice for the context panel, not a rule for all line plots. In both panels use the values passed to your function.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Plot `days` and `celsius` as a marked line on both axes.
2. Set the left y-axis lower bound to zero; set the right bounds to `focus` and title it `Detail view`.
