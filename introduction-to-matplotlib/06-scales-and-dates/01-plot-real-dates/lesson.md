---
title: "Use calendar dates on a line"
slug: plot-real-dates
order: 1
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Use calendar dates on a line using an explicit Matplotlib Figure and Axes."
seo_title: "Use calendar dates on a line | Neighborhood Signals Matplotlib"
seo_description: "A street tree crew tracks watered trees on named dates. Convert the day column to real dates so the x-axis has calendar spacing, not text categories."
seo_keywords: ["matplotlib", "python charts", "plot real dates"]
---
A street tree crew tracks watered trees on named dates. Convert the day column to real dates so the x-axis has calendar spacing, not text categories.

Convert with `pd.to_datetime`, then pass the dates and counts to `ax.plot`. Change the marker to squares to show each observation.

![Date strings become calendar positions rather than equally spaced categories.](dates-as-positions.svg)

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Change the plotted marker to `s` while keeping real calendar dates on the x-axis.
