---
title: "Frame the hours with ticks and limits"
slug: frame-hours-with-ticks
order: 9
language: python
lesson_type: coding
pyodide_packages: [matplotlib]
summary: "ax.set_xticks(hours) chooses printed tick positions. ax.set_xlim(left, right) sets the visible horizontal span without changing the data."
seo_title: "Frame the hours with ticks and limits | Beginner Matplotlib"
seo_description: "ax.set_xticks(hours) chooses printed tick positions. ax.set_xlim(left, right) sets the visible horizontal span without changing the data."
seo_keywords: ["Matplotlib", "Python charts", "frame hours with ticks"]
---
The garden log is sampled at specific hours; show those hours explicitly along the bottom.

`ax.set_xticks(hours)` chooses printed tick positions. `ax.set_xlim(left, right)` sets the visible horizontal span without changing the data.

Edit `main.py`, press **Run** and inspect the chart, then **Submit** to check your change. If the chart looks unchanged, inspect the line or label named in the task.

## Your Tasks

1. Extend the right x limit from 13 to 14; keep ticks at the sampled hours.
