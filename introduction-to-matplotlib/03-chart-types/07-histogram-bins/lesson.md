---
title: "Count temperatures in bins"
slug: histogram-bins
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "A gardener wants to see how often different temperatures occurred."
seo_title: "Count temperatures in bins | Python Charts"
seo_description: "`ax.hist(readings, bins=edges)` groups numeric measurements into adjacent intervals. Bar height counts readings, not the original temperature. The last interval includes its right edge."
seo_keywords: [Python charts, matplotlib, "histogram bins"]
hints:
  - "The list of bin boundaries belongs in the `bins` argument."
---
A gardener wants to see how often different temperatures occurred.

`ax.hist(readings, bins=edges)` groups numeric measurements into adjacent intervals. Bar height counts readings, not the original temperature. The last interval includes its right edge.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Insert `15` so the bin edges become `[10, 15, 20, 25]`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
