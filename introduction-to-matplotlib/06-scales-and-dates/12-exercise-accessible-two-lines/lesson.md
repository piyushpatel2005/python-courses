---
title: "Exercise: Make two routes distinguishable"
slug: exercise-accessible-two-lines
order: 12
language: python
lesson_type: coding
pyodide_packages: ["matplotlib"]
summary: "Exercise: Make two routes distinguishable using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Make two routes distinguishable | Neighborhood Signals Matplotlib"
seo_description: "A school compares morning walkers and riders on the same days. Build a compact chart that stays understandable if its colors look similar or it is printed in grayscale."
seo_keywords: ["matplotlib", "python charts", "exercise accessible two lines"]
---
A school compares morning walkers and riders on the same days. Build a compact chart that stays understandable if its colors look similar or it is printed in grayscale.

Give each series its own color and line pattern, add a legend, and leave room for labels with a constrained layout. A temporary style context does not alter later plots.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_school_routes`, plot both `walkers` and `riders` against `days` using distinct colors and solid versus dashed line patterns.
2. Name the lines `Walkers` and `Riders` in a visible legend.
3. Use the `ggplot` style inside a style context and enable constrained layout on the figure.
