---
title: "Exercise: Note the busiest hour"
slug: exercise-note-busiest-hour
order: 12
language: python
lesson_type: coding
pyodide_packages: [matplotlib]
summary: "Find the position of the largest count, then use that position to choose its hour. Point a note to the data point; place its text three counts ab"
seo_title: "Exercise: Note the busiest hour | Beginner Matplotlib"
seo_description: "Find the position of the largest count, then use that position to choose its hour. Point a note to the data point; place its text three counts ab"
seo_keywords: ["Matplotlib", "Python charts", "exercise note busiest hour"]
---
The library wants to flag the highest visitor count in each branch chart.

Find the position of the largest count, then use that position to choose its hour. Point a note to the data point; place its text three counts above.

Edit `main.py`, press **Run** and inspect the chart, then **Submit** to check your change. If the chart looks unchanged, inspect the line or label named in the task.

## Your Tasks

1. Complete `busiest_hour(hours, counts)` to plot the inputs, annotate the first maximum with text `"Peak: {count}"` at `(hour, count)`, place the note at `(hour, count + 3)` with an arrow, and return the figure.
