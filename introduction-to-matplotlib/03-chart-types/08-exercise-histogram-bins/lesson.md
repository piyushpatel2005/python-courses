---
title: "Group bus waiting times"
slug: exercise-histogram-bins
order: 8
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "A bus shelter logs individual waiting times in minutes."
seo_title: "Group bus waiting times | Python Charts"
seo_description: "Build a histogram from raw observations; the supplied edge list defines the intervals."
seo_keywords: [Python charts, matplotlib, "exercise histogram bins"]
hints:
  - "Call `ax.hist(waits, bins=edges)`; do not count the intervals yourself."
---
A bus shelter logs individual waiting times in minutes.

Build a histogram from raw observations; the supplied edge list defines the intervals.

The starter shows each wait as a dot along the baseline. Replace those dots with bars that count waits in each interval.

## Your Task

1. Replace the dot strip in `wait_hist(waits, edges)` with a histogram using the supplied bins and label the horizontal axis `Wait (minutes)`.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
