---
title: "Exercise: Compare two table columns"
slug: exercise-scatter-columns
order: 10
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Exercise: Compare two table columns using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Compare two table columns | Neighborhood Signals Matplotlib"
seo_description: "The playground team compares tree cover with summer temperature. Preserve each row as a pair in a scatter plot."
seo_keywords: ["matplotlib", "python charts", "exercise scatter columns"]
---
The playground team compares tree cover with summer temperature. Preserve each row as a pair in a scatter plot.

Use `frame["canopy_pct"]` for x and `frame["temp_c"]` for y; do not sort the columns independently.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_canopy_temperature`, scatter every row as its `(canopy_pct, temp_c)` pair.
2. Label the axes `Canopy (%)` and `Temperature (°C)`.
