---
title: "Size a garden trend"
slug: exercise-figure-size
order: 2
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "A garden chart has long weekday labels and needs a taller canvas."
seo_title: "Size a garden trend | Python Charts"
seo_description: "Give the whole Figure enough room before adding the readings."
seo_keywords: [Python charts, matplotlib, "exercise figure size"]
hints:
  - "Set the size in `plt.subplots`, then call `ax.plot`."
---
A garden chart has long weekday labels and needs a taller canvas.

Give the whole Figure enough room before adding the readings.

Use the preceding example as a pattern, but build this chart from the new observations. The function accepts new data, so the same chart works for other observations.

## Your Task

1. Complete `garden_canvas(days, temperature)` with Figure size `(7, 4)` and a line through the supplied data.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
