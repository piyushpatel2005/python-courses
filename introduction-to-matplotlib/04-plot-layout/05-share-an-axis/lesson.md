---
title: "Align days across panels"
slug: share-an-axis
order: 5
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "Two transit measures recorded on the same days should stay aligned when viewed together."
seo_title: "Align days across panels | Python Charts"
seo_description: "`sharex=True` gives vertically stacked panels the same x scale; moving one x limit also updates the other. Their y scales remain independent."
seo_keywords: [Python charts, matplotlib, "share an axis"]
hints:
  - "Pass the sharing option in `plt.subplots(2, 1, ...)`."
---
Two transit measures recorded on the same days should stay aligned when viewed together.

`sharex=True` gives vertically stacked panels the same x scale; moving one x limit also updates the other. Their y scales remain independent.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Change `sharex=False` to `sharex=True`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
