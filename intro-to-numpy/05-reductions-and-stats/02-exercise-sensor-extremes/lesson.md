---
title: "Locate sensor extremes"
slug: exercise-sensor-extremes
order: 2
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Locate sensor extremes with NumPy arrays."
seo_title: "Locate sensor extremes | Intro to NumPy"
seo_description: "Practice locate sensor extremes in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, statistics]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

The pocket observatory stores brightness readings in arrival order. The smallest and largest values and their indices answer different questions. 

Type the technique in `main.py`, press Run to inspect the result, then Submit.

## Your Task

1. Implement `extremes(readings)` with NumPy reductions and `argmin`/`argmax`; return the five results in the documented order.
