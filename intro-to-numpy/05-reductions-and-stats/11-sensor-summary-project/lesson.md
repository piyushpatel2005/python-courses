---
title: "Project: read the panel"
slug: sensor-summary-project
order: 11
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Build the panel report with night totals and sensor means."
seo_title: "Project: read the panel | Intro to NumPy"
seo_description: "Build the panel report with night totals and sensor means."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'Means accept an `axis` argument too; a sensor history runs down a column.'
---

The Pocket Observatory needs a report for a grid with one night per row and one sensor per column. Start with total light per night and average reading per sensor.

`np.mean` accepts `axis` just as `np.sum` does. Choose the dimension to collapse: totals per night need axis 1, while means per sensor need axis 0. Fill the two placeholders; the tuple and sample print are supplied.

## Your Tasks

1. Set `night_totals` to the sum of each row in `grid`.
2. Set `sensor_means` to the mean of each column in `grid`.

Run `main.py`: expect night totals `[12 18]` and sensor means `[6. 4.5 4.5]`. Submit, then continue with the same panel in the next lesson.
