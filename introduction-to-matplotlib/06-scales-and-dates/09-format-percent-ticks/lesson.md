---
title: "Format proportions as percentages"
slug: format-percent-ticks
order: 9
language: python
lesson_type: coding
pyodide_packages: ["matplotlib"]
summary: "Format proportions as percentages using an explicit Matplotlib Figure and Axes."
seo_title: "Format proportions as percentages | Neighborhood Signals Matplotlib"
seo_description: "The recycling share is stored as a fraction from zero to one. Format tick labels as percentages while keeping fractional data unchanged."
seo_keywords: ["matplotlib", "python charts", "format percent ticks"]
---
The recycling share is stored as a fraction from zero to one. Format tick labels as percentages while keeping fractional data unchanged.

`PercentFormatter(xmax=1, decimals=...)` converts display labels only. Remove the decimal place from the y tick labels.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Set the percent tick formatter to `decimals=0`.
