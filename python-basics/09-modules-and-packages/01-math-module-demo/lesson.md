---
title: 'Demo: Calculate Beacon Capacity'
slug: math-module-demo
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: 'Use math.ceil to round up a beacon capacity calculation.'
seo_title: 'Demo: Calculate Beacon Capacity | Python Basics'
seo_description: 'Use math.ceil to round up a beacon capacity calculation.'
seo_keywords: [python basics, math module demo, python practice]
hints:
  - Change the number in the bottom call, not the divisor.
---

The Tool Library has code you can reuse. Python's standard library includes `math`, a module of mathematical tools. `import math` makes the name `math` available; the dot in `math.ceil(...)` selects its `ceil` function.

`ceil` rounds up. Each beacon holds four sparks, so eleven sparks need three beacons even though the third is only partly full.

Change the final call in `main.py` from `8` to `11`. Run should change from `2` to `3`, then Submit.

## Your Task

1. Change the final `beacons_needed` call to use `11` sparks.
