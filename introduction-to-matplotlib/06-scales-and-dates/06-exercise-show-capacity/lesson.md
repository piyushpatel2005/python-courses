---
title: "Exercise: Frame the bike rack count"
slug: exercise-show-capacity
order: 6
language: python
lesson_type: coding
pyodide_packages: ["matplotlib"]
summary: "Exercise: Frame the bike rack count using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Frame the bike rack count | Neighborhood Signals Matplotlib"
seo_description: "The bike rack team compares filled spaces through the day against rack capacity. Let the caller provide capacity so the chart is reusable."
seo_keywords: ["matplotlib", "python charts", "exercise show capacity"]
---
The bike rack team compares filled spaces through the day against rack capacity. Let the caller provide capacity so the chart is reusable.

The supplied `capacity` is at least as large as every count. Start y at zero and end exactly at the supplied capacity; include people-friendly units.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_rack_use`, plot `hours` against `bikes` and set the y-axis from zero to `capacity`.
2. Label the axes `Hour of day` and `Bikes (count)`.
