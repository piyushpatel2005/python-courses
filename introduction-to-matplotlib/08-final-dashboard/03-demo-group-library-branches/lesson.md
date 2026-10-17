---
title: 'Demo: Group library branches'
slug: demo-group-library-branches
order: 3
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Aggregate visits by branch before drawing one bar per branch.'
seo_title: 'Demo: Group library branches | Introduction to Matplotlib'
seo_description: 'Aggregate visits by branch before drawing one bar per branch.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'demo'
  - 'group'
  - 'library'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Demo: Group library branches

A branch appears on more than one day, so raw rows are not yet a branch comparison. `groupby('branch')['visits'].sum()` combines each branch's daily totals. Set the lower axis bound to zero, then confirm the bars reflect grouped totals rather than single rows.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Start the visits y-axis at zero in `branch_totals(frame)`.
