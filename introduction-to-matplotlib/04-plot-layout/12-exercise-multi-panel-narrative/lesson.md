---
title: "Finish a weekly neighborhood brief"
slug: exercise-multi-panel-narrative
order: 12
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "The brief already charts garden temperature and library visits; add transit boardings as the final panel."
seo_title: "Finish a weekly neighborhood brief | Python Charts"
seo_description: "Keep one coherent Figure title, but give each question its own Axes."
seo_keywords: [Python charts, matplotlib, "exercise multi panel narrative"]
hints:
  - "Draw `axes[2].bar(days, transit)` and set its title."
---
The brief already charts garden temperature and library visits; add transit boardings as the final panel.

Keep one coherent Figure title, but give each question its own Axes.

Use the preceding example as a pattern, but build this chart from the new observations. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Complete the third panel of `weekly_story(days, garden, library, transit)` with transit bars, title it `Transit boardings`, and keep the supplied two panels unchanged.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
