---
title: "Use the Series index as the x-axis"
slug: plot-series-index
order: 3
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Use the Series index as the x-axis using an explicit Matplotlib Figure and Axes."
seo_title: "Use the Series index as the x-axis | Neighborhood Signals Matplotlib"
seo_description: "The community greenhouse already stores readings as a Pandas Series. Its index names the observation days, while its values give the readings."
seo_keywords: ["matplotlib", "python charts", "plot series index"]
---
The community greenhouse already stores readings as a Pandas Series. Its index names the observation days, while its values give the readings.

Pass `series.index` and `series.to_numpy()` separately to `ax.plot`. Change the marker from circles to squares to make each observation easy to pick out.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Change the plotted marker from `o` to `s`, keeping the Series index on the x-axis.
