---
title: "Name each panel explicitly"
slug: label-each-panel
order: 9
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "Two garden readings use different units, so each panel needs its own heading."
seo_title: "Name each panel explicitly | Python Charts"
seo_description: "Call `set_title` and `set_ylabel` on the specific Axes, not on the whole Figure. Lettered titles make panels easy to refer to in a report."
seo_keywords: [Python charts, matplotlib, "label each panel"]
hints:
  - "Use `axes[1].set_title(...)` for the right panel."
---
Two garden readings use different units, so each panel needs its own heading.

Call `set_title` and `set_ylabel` on the specific Axes, not on the whole Figure. Lettered titles make panels easy to refer to in a report.

The starter already draws a figure. Make one small edit, then compare the visible chart. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Change the second title to `(b) Moisture`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
