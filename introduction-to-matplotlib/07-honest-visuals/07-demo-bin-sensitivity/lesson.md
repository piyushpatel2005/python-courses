---
title: 'Demo: Change histogram bins'
slug: demo-bin-sensitivity
order: 7
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'See how a bin choice changes a distribution without changing observations.'
seo_title: 'Demo: Change histogram bins | Introduction to Matplotlib'
seo_description: 'See how a bin choice changes a distribution without changing observations.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'demo'
  - 'change'
  - 'histogram'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Demo: Change histogram bins

The transit stop recorded wait times. A histogram counts observations within intervals. Few bins smooth over detail; many bins can suggest a pattern from sparse data. Change the bin count, then compare shapes while keeping the data and range fixed. The count of observations should remain constant.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Use five equal-width bins for `wait_histogram(waits)`.
