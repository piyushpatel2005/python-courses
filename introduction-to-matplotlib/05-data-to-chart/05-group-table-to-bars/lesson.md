---
title: "Group a table before drawing bars"
slug: group-table-to-bars
order: 5
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Group a table before drawing bars using an explicit Matplotlib Figure and Axes."
seo_title: "Group a table before drawing bars | Neighborhood Signals Matplotlib"
seo_description: "Several observations belong to each park. Compute the mean visitor count per park before drawing one bar for each group."
seo_keywords: ["matplotlib", "python charts", "group table to bars"]
---
Several observations belong to each park. Compute the mean visitor count per park before drawing one bar for each group.

`groupby("park")["visitors"].mean()` reduces repeated rows to one value per category. Change the title so the chart describes the aggregation, not just the raw table.

![Repeated table rows become one mean per category before plotting.](grouped-bars.svg)

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Set the title to `Mean visitors by park`.
