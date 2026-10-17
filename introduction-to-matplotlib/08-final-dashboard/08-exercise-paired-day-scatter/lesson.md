---
title: 'Exercise: Plot paired daily signals'
slug: exercise-paired-day-scatter
order: 8
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Merge cleaned daily records before plotting their relationship.'
seo_title: 'Exercise: Plot paired daily signals | Introduction to Matplotlib'
seo_description: 'Merge cleaned daily records before plotting their relationship.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'exercise'
  - 'plot'
  - 'paired'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Exercise: Plot paired daily signals

Make a reusable scatter plot. Each garden row is a daily temperature, and the library may have several branch rows per day. First sum library visits by day, then merge to garden on the common day. Only overlapping days become points. A dot indicates coincidence, not a cause.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Return matched `day, temp_c, visits` rows from `match_signals(garden, library)` after summing library visits by day.
2. Plot one scatter point per matched day, labeled in °C and visits, with a neutral title.
