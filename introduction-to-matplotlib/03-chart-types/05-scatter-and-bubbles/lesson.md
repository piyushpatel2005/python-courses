---
title: "Scatter points with a third measure"
slug: scatter-and-bubbles
order: 5
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "Each garden plot has sunlight, harvest, and planted area."
seo_title: "Scatter points with a third measure | Python Charts"
seo_description: "`ax.scatter(x, y, s=area)` locates each plot with two measurements and uses point area for a third. Use a moderate transparency when points overlap."
seo_keywords: [Python charts, matplotlib, "scatter and bubbles"]
hints:
  - "Set `alpha` on the scatter call, not on the whole figure."
---
Each garden plot has sunlight, harvest, and planted area.

`ax.scatter(x, y, s=area)` locates each plot with two measurements and uses point area for a third. Use a moderate transparency when points overlap.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Increase point transparency setting to `alpha=0.7`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
