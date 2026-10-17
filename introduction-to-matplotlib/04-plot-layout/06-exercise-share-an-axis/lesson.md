---
title: "Align garden measurements"
slug: exercise-share-an-axis
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "Garden temperature and soil moisture were measured on the same dates."
seo_title: "Align garden measurements | Python Charts"
seo_description: "Share only the horizontal days; each measurement needs its own vertical scale."
seo_keywords: [Python charts, matplotlib, "exercise share an axis"]
hints:
  - "Use `sharex=True` when making the two panels."
---
Garden temperature and soil moisture were measured on the same dates.

Share only the horizontal days; each measurement needs its own vertical scale.

Use the preceding example as a pattern, but build this chart from the new observations. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Complete `shared_garden(days, temperature, moisture)` with two stacked line panels that share their horizontal axis.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
