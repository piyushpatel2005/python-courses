---
title: "Vertical bars for category totals"
slug: vertical-bars
order: 1
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "Garden beds have separate harvest totals."
seo_title: "Vertical bars for category totals | Python Charts"
seo_description: "Use `ax.bar(categories, totals)` when the horizontal positions are named groups and bar height is the quantity. The bars start at zero, so comparing heights is straightforward."
seo_keywords: [Python charts, matplotlib, "vertical bars"]
hints:
  - "The color belongs in the `ax.bar(...)` call."
---
![A diagram of how the chart is organized](chart-question-map.svg)

Garden beds have separate harvest totals.

Use `ax.bar(categories, totals)` when the horizontal positions are named groups and bar height is the quantity. The bars start at zero, so comparing heights is straightforward.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Change the bar color to `seagreen`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
