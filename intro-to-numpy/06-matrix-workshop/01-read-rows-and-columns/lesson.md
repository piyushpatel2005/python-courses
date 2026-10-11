---
title: "Read the grid"
slug: read-rows-and-columns
order: 1
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: 'Follow one sensor down a night-by-sensor grid using a column slice.'
seo_title: "Read the grid | Intro to NumPy"
seo_description: 'Follow one sensor down a night-by-sensor grid using a column slice.'
seo_keywords: [numpy, arrays, matrices]
hints:
  - The colon keeps every row; the number after the comma picks a column.
---

The last section summarized whole sensor panels. Here, start by following one instrument through the nights. Rows still represent nights, and columns still represent sensors.

`grid[row, column]` selects one measurement. In `grid[:, column]`, the colon means “take every row.” The result is a one-dimensional history in the original night order. Column numbers start at zero, so column `1` belongs to the second sensor.

Run `main.py` to see the first sensor's history. Edit the `sensor_history` assignment, Run again to compare the readings, then Submit.

## Your Task

1. Select column `1` from `grid` with 2D slicing, storing the second sensor's history in `sensor_history`. The supplied print should show `[8 2]`.
