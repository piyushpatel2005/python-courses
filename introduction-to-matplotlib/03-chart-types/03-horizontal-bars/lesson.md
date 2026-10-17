---
title: "Horizontal bars for long names"
slug: horizontal-bars
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "Transit stop names can crowd a horizontal axis."
seo_title: "Horizontal bars for long names | Python Charts"
seo_description: "`ax.barh(names, values)` puts names on the vertical axis and values across the page. Width, rather than height, represents the count."
seo_keywords: [Python charts, matplotlib, "horizontal bars"]
hints:
  - "Call `ax.set_xlabel(\"Riders\")`."
---
Transit stop names can crowd a horizontal axis.

`ax.barh(names, values)` puts names on the vertical axis and values across the page. Width, rather than height, represents the count.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Change the horizontal-axis label to `Riders`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
