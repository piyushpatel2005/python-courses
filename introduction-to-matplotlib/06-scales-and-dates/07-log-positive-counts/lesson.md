---
title: "Use log scale for positive ranges"
slug: log-positive-counts
order: 7
language: python
lesson_type: coding
pyodide_packages: ["matplotlib"]
summary: "Use log scale for positive ranges using an explicit Matplotlib Figure and Axes."
seo_title: "Use log scale for positive ranges | Neighborhood Signals Matplotlib"
seo_description: "An event attendance series spans ones through thousands. A logarithmic y-axis can show multiplicative changes without flattening the smaller counts."
seo_keywords: ["matplotlib", "python charts", "log positive counts"]
---
An event attendance series spans ones through thousands. A logarithmic y-axis can show multiplicative changes without flattening the smaller counts.

Log scales cannot place zero or negative values: do not use them to hide missing or invalid observations. Extend the lower bound from 2 down to 1 to show the first event.

![A log axis marks equal ratios with equal distances; zero has no log position.](log-scale-ratios.svg)

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Set the logarithmic y-axis lower bound to 1 and keep its upper bound at 1000.
