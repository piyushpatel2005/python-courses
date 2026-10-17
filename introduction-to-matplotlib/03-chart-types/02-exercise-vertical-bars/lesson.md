---
title: "Build library visit bars"
slug: exercise-vertical-bars
order: 2
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "A library wants a chart comparing branch visits."
seo_title: "Build library visit bars | Python Charts"
seo_description: "Apply the vertical-bar pattern to a different set of category totals."
seo_keywords: [Python charts, matplotlib, "exercise vertical bars"]
hints:
  - "Use `ax.bar(branches, visits)` before returning the figure."
---
A library wants a chart comparing branch visits.

Apply the vertical-bar pattern to a different set of category totals.

The starter connects visits with a faint line. Replace that line rather than layering bars over it. The function accepts new data, so the chart works for other branches.

## Your Task

1. Replace the line in `library_bars(branches, visits)` with one vertical bar per branch and label the vertical axis `Visits`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
