---
title: "Point to a peak"
slug: point-to-the-peak
order: 11
language: python
lesson_type: coding
pyodide_packages: [matplotlib]
summary: "ax.annotate(text, xy=(x, y), xytext=(x, y + 3), arrowprops=...) attaches a note to a specific point. xy is the data location; xytext positions th"
seo_title: "Point to a peak | Beginner Matplotlib"
seo_description: "ax.annotate(text, xy=(x, y), xytext=(x, y + 3), arrowprops=...) attaches a note to a specific point. xy is the data location; xytext positions th"
seo_keywords: ["Matplotlib", "Python charts", "point to the peak"]
---
A windy noon reading is worth calling out without making readers hunt for it.

`ax.annotate(text, xy=(x, y), xytext=(x, y + 3), arrowprops=...)` attaches a note to a specific point. `xy` is the data location; `xytext` positions the note away from it.

Edit `main.py`, press **Run** and inspect the chart, then **Submit** to check your change. If the chart looks unchanged, inspect the line or label named in the task.

## Your Tasks

1. Change the annotation text from `"Noon"` to `"Wind peak"` while keeping its arrow at hour 12, reading 9.
