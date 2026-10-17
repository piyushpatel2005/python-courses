---
title: 'Project stage 2: Clean and combine'
slug: project-clean-and-combine
order: 10
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Create all four panels from cleaned, grouped, matched data.'
seo_title: 'Project stage 2: Clean and combine | Introduction to Matplotlib'
seo_description: 'Create all four panels from cleaned, grouped, matched data.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'project'
  - 'stage'
  - '2'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Project stage 2: Clean and combine

Stage 1 made the layout. Now make every panel reliable: drop incomplete readings, average duplicate garden measurements, sum valid library and transit counts, and match only shared garden/library days. Keep the bar baseline at zero and use a legend for each non-bar series. `prepare_signals` returns the tidy intermediates so the relationships remain inspectable. The starter already draws a rough three-panel dashboard; replace that rough aggregation rather than hand-entering numbers.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Return cleaned `garden_daily`, `branch_totals`, `transit_daily`, and `matched` from `prepare_signals`, grouping and joining by the proper keys.
2. Use those results to fill four panels (line, bar, line, scatter) with units, a zero bar baseline, and legends for plotted series.
