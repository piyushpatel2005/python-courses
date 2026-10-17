---
title: 'Demo: Start bars at zero'
slug: demo-bar-baseline
order: 1
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Set a zero baseline so garden counts are proportional to bar height.'
seo_title: 'Demo: Start bars at zero | Introduction to Matplotlib'
seo_description: 'Set a zero baseline so garden counts are proportional to bar height.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'demo'
  - 'start'
  - 'bars'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Demo: Start bars at zero

The team compares five and eight garden volunteers. Bars encode magnitude by length, so a vertical axis beginning at four makes eight look many times larger. The bars in `main.py` already draw; change only the baseline and compare the before and after views. A line chart may use a zoomed range, but a magnitude bar needs its zero.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Set the bar chart lower y-limit to zero inside `draw_volunteers(counts)`.

![Two bars of heights five and eight shown with a zero baseline and a misleading clipped baseline](bar-baseline.svg)
