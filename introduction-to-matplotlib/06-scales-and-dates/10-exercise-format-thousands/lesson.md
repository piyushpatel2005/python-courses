---
title: "Exercise: Format large visitor totals"
slug: exercise-format-thousands
order: 10
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Exercise: Format large visitor totals using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Format large visitor totals | Neighborhood Signals Matplotlib"
seo_description: "A plaza counter records visits in the thousands. Show comma-separated y-axis ticks without rewriting the underlying numbers."
seo_keywords: ["matplotlib", "python charts", "exercise format thousands"]
---
A plaza counter records visits in the thousands. Show comma-separated y-axis ticks without rewriting the underlying numbers.

Use `FuncFormatter` from `matplotlib.ticker`. It receives the tick value and its position; return a string such as `1,250` for 1250.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_large_visits`, draw one bar per site from the supplied table columns `site` and `visits`.
2. Format y-axis ticks as whole numbers with thousands separators, such as `1,250`.
