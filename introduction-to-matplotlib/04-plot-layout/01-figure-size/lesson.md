---
title: "Give a chart room to breathe"
slug: figure-size
order: 1
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "A library attendance line needs a wide space for day labels."
seo_title: "Give a chart room to breathe | Python Charts"
seo_description: "`figsize=(width, height)` sizes the Figure in inches. It changes the entire canvas, not the data coordinates."
seo_keywords: [Python charts, matplotlib, "figure size"]
hints:
  - "Pass `figsize=(8, 3)` to `plt.subplots()`."
---
![A diagram of how the chart is organized](figure-panel-map.svg)

A library attendance line needs a wide space for day labels.

`figsize=(width, height)` sizes the Figure in inches. It changes the entire canvas, not the data coordinates.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Change the Figure size to `(8, 3)`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
