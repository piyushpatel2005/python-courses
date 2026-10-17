---
title: "Exercise: Make collection dates readable"
slug: exercise-rotate-calendar-labels
order: 4
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Exercise: Make collection dates readable using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Make collection dates readable | Neighborhood Signals Matplotlib"
seo_description: "A neighborhood food drive publishes collection totals across several dates. Keep the date scale and tilt its labels for reading."
seo_keywords: ["matplotlib", "python charts", "exercise rotate calendar labels"]
---
A neighborhood food drive publishes collection totals across several dates. Keep the date scale and tilt its labels for reading.

The function takes a table with `day` and `bags`. The `day` strings must become dates before plotting.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_collection_dates`, plot dated `bags` as one line and rotate x-axis tick labels to 40 degrees.
2. Label the axes `Date` and `Collected bags (count)`.
