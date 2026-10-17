---
title: "Make room for a garden pair"
slug: exercise-constrained-layout
order: 8
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "Two garden panels need labels that do not crowd one another."
seo_title: "Make room for a garden pair | Python Charts"
seo_description: "Allow the Figure to arrange its margins while keeping one plot in each panel."
seo_keywords: [Python charts, matplotlib, "exercise constrained layout"]
hints:
  - "Set `constrained_layout=True` in `plt.subplots(1, 2, ...)`."
---
Two garden panels need labels that do not crowd one another.

Allow the Figure to arrange its margins while keeping one plot in each panel.

Use the preceding example as a pattern, but build this chart from the new observations. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Complete `garden_pair(days, sunshine, rain)` with two side-by-side line panels and constrained layout enabled.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
