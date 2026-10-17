---
title: "Drop incomplete pairs, not entire columns"
slug: missing-pairs-and-units
order: 11
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Drop incomplete pairs, not entire columns using an explicit Matplotlib Figure and Axes."
seo_title: "Drop incomplete pairs, not entire columns | Neighborhood Signals Matplotlib"
seo_description: "A volunteer survey has missing garden temperatures and walker counts. Keep only rows where *both* coordinates exist so each scatter point represents one observation."
seo_keywords: ["matplotlib", "python charts", "missing pairs and units"]
---
A volunteer survey has missing garden temperatures and walker counts. Keep only rows where *both* coordinates exist so each scatter point represents one observation.

`dropna(subset=[...])` filters rows together. Change the x-axis label to include the temperature unit; a bare number can mean Celsius or Fahrenheit.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Set the x-axis label to `Temperature (°C)` while retaining only complete `(temperature, walkers)` pairs.
