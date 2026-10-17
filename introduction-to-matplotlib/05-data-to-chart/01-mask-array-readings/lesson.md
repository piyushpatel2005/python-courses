---
title: "Filter readings with a NumPy mask"
slug: mask-array-readings
order: 1
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "numpy"]
summary: "Filter readings with a NumPy mask using an explicit Matplotlib Figure and Axes."
seo_title: "Filter readings with a NumPy mask | Neighborhood Signals Matplotlib"
seo_description: "The garden desk only needs readings above a heat threshold. A Boolean mask selects matching days and temperatures together."
seo_keywords: ["matplotlib", "python charts", "mask array readings"]
---
The garden desk only needs readings above a heat threshold. A Boolean mask selects matching days and temperatures together.

The two arrays must share a mask; filtering only the temperatures would pair them with the wrong days. Change the threshold from 27 to 29 and see the one remaining point.

![The same mask selects corresponding positions in the day and temperature arrays.](aligned-mask.svg)

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Change `threshold` to 29 so the chart keeps only readings strictly above 29 °C.
