---
title: "Exercise: Mask a new sensor series"
slug: exercise-mask-array-readings
order: 2
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "numpy"]
summary: "Exercise: Mask a new sensor series using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Mask a new sensor series | Neighborhood Signals Matplotlib"
seo_description: "The riverside sensor reports different days and noise levels. Build a reusable chart that filters both arrays using the same threshold."
seo_keywords: ["matplotlib", "python charts", "exercise mask array readings"]
---
The riverside sensor reports different days and noise levels. Build a reusable chart that filters both arrays using the same threshold.

The function receives arrays of equal length. Use a strict `>` comparison; a value equal to the threshold does not appear.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_loud_days`, select matching `days` and `decibels` above `threshold`, then plot the selected pairs on `ax`.
2. Label the x-axis `Day` and the y-axis `Noise (dB)`.
