---
title: "Exercise: Plot a labeled Series"
slug: exercise-plot-series
order: 4
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Exercise: Plot a labeled Series using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Plot a labeled Series | Neighborhood Signals Matplotlib"
seo_description: "A block captain shares library visits indexed by neighborhood name. Reuse the Series index instead of inventing positions 0, 1, 2."
seo_keywords: ["matplotlib", "python charts", "exercise plot series"]
---
A block captain shares library visits indexed by neighborhood name. Reuse the Series index instead of inventing positions 0, 1, 2.

An index may contain any labels. The hidden checks use different labels and values, so keep the function dependent on its argument.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_visits`, plot the supplied Series index against its values with circle markers.
2. Set the x-axis label to `Neighborhood` and the y-axis label to `Visits (people)`.
