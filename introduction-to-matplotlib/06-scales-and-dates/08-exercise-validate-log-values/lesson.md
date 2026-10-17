---
title: "Exercise: Plot a positive range"
slug: exercise-validate-log-values
order: 8
language: python
lesson_type: coding
pyodide_packages: ["matplotlib"]
summary: "Exercise: Plot a positive range using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Plot a positive range | Neighborhood Signals Matplotlib"
seo_description: "Local events vary greatly in attendance. Compare them on a log scale, but reject data that cannot appear honestly on that scale."
seo_keywords: ["matplotlib", "python charts", "exercise validate log values"]
---
Local events vary greatly in attendance. Compare them on a log scale, but reject data that cannot appear honestly on that scale.

Before plotting, reject any value at or below zero with `ValueError`. Do not replace those values with invented positive counts.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_event_range`, draw bars for the supplied labels and positive `counts` on a logarithmic y-axis.
2. Raise `ValueError` when any count is zero or negative.
