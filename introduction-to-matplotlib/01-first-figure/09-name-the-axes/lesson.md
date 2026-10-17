---
title: "Name both axes"
slug: name-the-axes
order: 9
language: python
lesson_type: coding
pyodide_packages: [matplotlib]
summary: "ax.set_xlabel(...) describes the horizontal values; ax.set_ylabel(...) describes the vertical values. The names belong to the axes, not to each i"
seo_title: "Name both axes | Beginner Matplotlib"
seo_description: "ax.set_xlabel(...) describes the horizontal values; ax.set_ylabel(...) describes the vertical values. The names belong to the axes, not to each i"
seo_keywords: ["Matplotlib", "Python charts", "name the axes"]
---
A garden chart needs units so readers do not mistake humidity for temperature.

`ax.set_xlabel(...)` describes the horizontal values; `ax.set_ylabel(...)` describes the vertical values. The names belong to the axes, not to each individual line.

Edit `main.py`, press **Run** and inspect the chart, then **Submit** to check your change. If the chart looks unchanged, inspect the line or label named in the task.

## Your Tasks

1. Change the vertical label from `"Reading"` to `"Humidity (%)"`.
