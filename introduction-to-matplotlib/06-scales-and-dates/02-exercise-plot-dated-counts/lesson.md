---
title: "Exercise: Draw a dated visit trend"
slug: exercise-plot-dated-counts
order: 2
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Exercise: Draw a dated visit trend using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Draw a dated visit trend | Neighborhood Signals Matplotlib"
seo_description: "The center sends visits with ISO-formatted date strings. Convert and sort by actual date before joining observations."
seo_keywords: ["matplotlib", "python charts", "exercise plot dated counts"]
---
The center sends visits with ISO-formatted date strings. Convert and sort by actual date before joining observations.

Use `pd.to_datetime` and `sort_values` on the full table so each visit count stays with its day.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_dated_visits`, convert `day` to dates, sort the paired rows chronologically, and plot one line against `visits`.
2. Label the axes `Date` and `Visits (people)`.
