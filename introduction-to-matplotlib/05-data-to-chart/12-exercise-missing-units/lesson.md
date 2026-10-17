---
title: "Exercise: Chart complete rain observations"
slug: exercise-missing-units
order: 12
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Exercise: Chart complete rain observations using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Chart complete rain observations | Neighborhood Signals Matplotlib"
seo_description: "The neighborhood rain log has blank readings. Only plot rows with both rainfall and visitor counts; do not let missing values silently shift one column against the other."
seo_keywords: ["matplotlib", "python charts", "exercise missing units"]
---
The neighborhood rain log has blank readings. Only plot rows with both rainfall and visitor counts; do not let missing values silently shift one column against the other.

Filter the whole DataFrame with `dropna(subset=["rain_mm", "visitors"])` before selecting columns. The labels state the units of both observations.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_rain_visitors`, scatter the complete `(rain_mm, visitors)` pairs only.
2. Label the axes `Rainfall (mm)` and `Visitors (people)`.
