---
title: "Summarize journey times"
slug: exercise-boxplot-spread
order: 10
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "A transit planner needs to compare typical trip time with its spread."
seo_title: "Summarize journey times | Python Charts"
seo_description: "Pass the raw minutes into one boxplot; the median line should come from the data."
seo_keywords: [Python charts, matplotlib, "exercise boxplot spread"]
hints:
  - "Use `patch_artist=True` to make the box a filled patch."
---
A transit planner needs to compare typical trip time with its spread.

Pass the raw minutes into one boxplot; the median line should come from the data.

The starter shows each trip as a dot. Replace the dot strip with a boxplot so the middle and spread are easier to compare.

## Your Task

1. Replace the dots in `trip_boxplot(minutes)` with a filled boxplot and label the vertical axis `Trip (minutes)`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
