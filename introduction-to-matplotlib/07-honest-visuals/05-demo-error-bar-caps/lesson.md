---
title: 'Demo: Read uncertainty bars'
slug: demo-error-bar-caps
order: 5
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Show a measurement and its spread with capped error bars.'
seo_title: 'Demo: Read uncertainty bars | Introduction to Matplotlib'
seo_description: 'Show a measurement and its spread with capped error bars.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'demo'
  - 'read'
  - 'uncertainty'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Demo: Read uncertainty bars

Garden sensors report a daily estimate and a margin. An error bar is an interval around that estimate, not another observation and not proof of statistical significance. `yerr` already supplies the half-width for each point. Change the cap width so the intervals are easier to see.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Set `capsize=5` in the `errorbar` call.
