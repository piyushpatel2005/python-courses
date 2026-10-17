---
title: "Combine style, color, pattern, and legend"
slug: style-color-pattern-legend
order: 11
language: python
lesson_type: coding
pyodide_packages: ["matplotlib"]
summary: "Combine style, color, pattern, and legend using an explicit Matplotlib Figure and Axes."
seo_title: "Combine style, color, pattern, and legend | Neighborhood Signals Matplotlib"
seo_description: "Two neighborhood pickup routes share one chart. Color and line pattern together distinguish them, and a legend names each route."
seo_keywords: ["matplotlib", "python charts", "style color pattern legend"]
---
Two neighborhood pickup routes share one chart. Color and line pattern together distinguish them, and a legend names each route.

Use a temporary `ggplot` style context instead of changing every future chart. The second route currently shares the first route’s solid pattern; make it dashed.

![Color plus line pattern and legend identify two signals without relying on color alone.](color-pattern-legend.svg)

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Change the second line to a dashed `--` pattern while retaining both legend labels.
