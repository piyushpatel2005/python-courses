---
title: "Summarize soil moisture spread"
slug: boxplot-spread
order: 9
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "The garden recorded many soil readings; its team needs a compact summary."
seo_title: "Summarize soil moisture spread | Python Charts"
seo_description: "A boxplot shows the median, the central half of readings, and whiskers. `showmeans=True` also marks the arithmetic mean, which can differ from the median."
seo_keywords: [Python charts, matplotlib, "boxplot spread"]
hints:
  - "Change the keyword in `ax.boxplot(...)`."
---
The garden recorded many soil readings; its team needs a compact summary.

A boxplot shows the median, the central half of readings, and whiskers. `showmeans=True` also marks the arithmetic mean, which can differ from the median.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Change `showmeans` to `True` so the mean marker appears.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
