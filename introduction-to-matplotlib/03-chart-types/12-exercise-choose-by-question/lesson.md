---
title: "Pick a neighborhood view"
slug: exercise-choose-by-question
order: 12
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "A library desk needs two answers from one set of observations."
seo_title: "Pick a neighborhood view | Python Charts"
seo_description: "For a comparison of named branches, use horizontal bars. For a distribution of numeric visit counts, use a histogram."
seo_keywords: [Python charts, matplotlib, "exercise choose by question"]
hints:
  - "Use `ax.barh` for comparison and `ax.hist(..., bins=3)` for distribution."
---
A library desk needs two answers from one set of observations.

For a comparison of named branches, use horizontal bars. For a distribution of numeric visit counts, use a histogram.

The starter sketches each answer with points. Replace those sketches with chart types that match the question instead of layering new artists over them.

## Your Task

1. Replace both sketches in `neighborhood_view(question, names, values)`: `"compare"` draws horizontal bars; `"distribution"` draws a three-bin histogram.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
