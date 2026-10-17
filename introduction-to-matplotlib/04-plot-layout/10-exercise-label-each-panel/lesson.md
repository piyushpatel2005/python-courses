---
title: "Label a community comparison"
slug: exercise-label-each-panel
order: 10
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "The board will place garden and library counts next to each other."
seo_title: "Label a community comparison | Python Charts"
seo_description: "Give each panel its own lettered title and a matching unit label."
seo_keywords: [Python charts, matplotlib, "exercise label each panel"]
hints:
  - "Set each title and y label on the Axes that owns that series."
---
The board will place garden and library counts next to each other.

Give each panel its own lettered title and a matching unit label.

Use the preceding example as a pattern, but build this chart from the new observations. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Complete `community_panels(days, beds, visits)` with two line panels titled `(a) Garden` and `(b) Library`, with vertical labels `Beds watered` and `Visits` respectively.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
