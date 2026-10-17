---
title: "Map reading activity"
slug: exercise-scatter-and-bubbles
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "A library records how visits vary by open hours; event attendance sizes each point."
seo_title: "Map reading activity | Python Charts"
seo_description: "Use the x and y positions for two measures, then point size for the third."
seo_keywords: [Python charts, matplotlib, "exercise scatter and bubbles"]
hints:
  - "Pass `s=events` to `ax.scatter(...)`."
---
A library records how visits vary by open hours; event attendance sizes each point.

Use the x and y positions for two measures, then point size for the third.

The starter connects its points with a line. Replace the line with separate bubbles so size can show event attendance.

## Your Task

1. Replace the connected line in `reading_bubbles(hours, visits, events)` with one scatter collection sized by `events` and label the horizontal axis `Open hours`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
