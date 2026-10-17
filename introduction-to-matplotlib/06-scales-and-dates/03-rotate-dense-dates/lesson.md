---
title: "Rotate crowded date labels"
slug: rotate-dense-dates
order: 3
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Rotate crowded date labels using an explicit Matplotlib Figure and Axes."
seo_title: "Rotate crowded date labels | Neighborhood Signals Matplotlib"
seo_description: "Daily library returns crowd the bottom edge of the chart. Rotate the x-axis tick labels so adjacent dates remain legible."
seo_keywords: ["matplotlib", "python charts", "rotate dense dates"]
---
Daily library returns crowd the bottom edge of the chart. Rotate the x-axis tick labels so adjacent dates remain legible.

`ax.tick_params(axis="x", labelrotation=...)` changes label orientation without changing the observations. Try 45 degrees instead of 20.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Rotate the date tick labels to 45 degrees.
