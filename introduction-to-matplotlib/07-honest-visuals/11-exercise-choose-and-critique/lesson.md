---
title: 'Project: Choose charts and critique them'
slug: exercise-choose-and-critique
order: 11
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Choose bars for categories and scatter for paired numeric observations.'
seo_title: 'Project: Choose charts and critique them | Introduction to Matplotlib'
seo_description: 'Choose bars for categories and scatter for paired numeric observations.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'project'
  - 'choose'
  - 'charts'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Project: Choose charts and critique them

The review board has two questions: which library branch had more visits, and whether hotter garden days tended to coincide with more visitors. Use bars for the categorical comparison and scatter for paired numbers; a line would imply an order the branch names do not have. A scatter association alone does not establish that heat *caused* library attendance. Label both panels and keep the bar baseline honest.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Build left-panel bars from `branches` and `visits`, with a zero baseline and `Visits` y-axis.
2. Build right-panel scatter from `temperatures` and `visitors`, with `Temperature (°C)` and `Visitors` axis labels.

A chart should answer its stated question without concealing observations, units, or a meaningful baseline. Carry that standard into the final dashboard.
