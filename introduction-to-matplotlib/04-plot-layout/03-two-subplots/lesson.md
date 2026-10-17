---
title: "Place two signals in one Figure"
slug: two-subplots
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "Library visits and transit boardings share the same week but deserve separate scales."
seo_title: "Place two signals in one Figure | Python Charts"
seo_description: "`plt.subplots(2, 1)` returns a Figure and two Axes arranged in rows. Each Axes receives only its own data."
seo_keywords: [Python charts, matplotlib, "two subplots"]
hints:
  - "Set the title on `axes[0]`."
---
Library visits and transit boardings share the same week but deserve separate scales.

`plt.subplots(2, 1)` returns a Figure and two Axes arranged in rows. Each Axes receives only its own data.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Change the upper panel title to `Library visits`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
