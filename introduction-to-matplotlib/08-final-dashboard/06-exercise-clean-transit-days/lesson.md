---
title: 'Exercise: Clean transit totals'
slug: exercise-clean-transit-days
order: 6
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Ignore missing ride counts and plot daily route sums.'
seo_title: 'Exercise: Clean transit totals | Introduction to Matplotlib'
seo_description: 'Ignore missing ride counts and plot daily route sums.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'exercise'
  - 'clean'
  - 'transit'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Exercise: Clean transit totals

The transit table has `day`, `route`, and `rides`. Do not silently count a missing ride value as a zero-rider route; drop incomplete observations, then sum valid rides by day. Return the tidy day/totals table and draw a line from it.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Return a `day, rides` DataFrame from `daily_transit(frame)`, sorted by day, after dropping rows missing any of `day`, `route`, or `rides`.
2. Plot daily ride sums with visible markers and a `Rides` y-axis.
