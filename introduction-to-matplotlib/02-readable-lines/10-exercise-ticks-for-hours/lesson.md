---
title: "Exercise: Frame library hours"
slug: exercise-ticks-for-hours
order: 10
language: python
lesson_type: coding
pyodide_packages: [matplotlib]
summary: "Use the supplied hours for ticks. Leave one hour of space on each side of the earliest and latest reading."
seo_title: "Exercise: Frame library hours | Beginner Matplotlib"
seo_description: "Use the supplied hours for ticks. Leave one hour of space on each side of the earliest and latest reading."
seo_keywords: ["Matplotlib", "Python charts", "exercise ticks for hours"]
---
Each library branch sends its own sampled hours, so fixed tick positions would mislabel another branch.

Use the supplied `hours` for ticks. Leave one hour of space on each side of the earliest and latest reading.

Edit `main.py`, press **Run** and inspect the chart, then **Submit** to check your change. If the chart looks unchanged, inspect the line or label named in the task.

## Your Tasks

1. Complete `hour_window(hours, counts)` to plot the inputs, set x ticks to `hours`, set x limits to one hour below the minimum and above the maximum, and return the figure.
