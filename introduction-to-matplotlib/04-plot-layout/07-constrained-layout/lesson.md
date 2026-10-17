---
title: "Keep panel labels clear"
slug: constrained-layout
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "Long transit panel titles need breathing room."
seo_title: "Keep panel labels clear | Python Charts"
seo_description: "`constrained_layout=True` asks the Figure to make room for titles and axis labels. It adjusts spacing without changing the data."
seo_keywords: [Python charts, matplotlib, "constrained layout"]
hints:
  - "Change the option inside `plt.subplots(...)`."
---
Long transit panel titles need breathing room.

`constrained_layout=True` asks the Figure to make room for titles and axis labels. It adjusts spacing without changing the data.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Enable `constrained_layout=True` on the Figure.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
