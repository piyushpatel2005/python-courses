---
title: 'Size a row of floor tiles'
slug: math-module-demo
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: 'Use math.ceil to round up a tile calculation.'
seo_title: 'Size a row of floor tiles | Python Basics'
seo_description: 'Use math.ceil to round up a tile calculation.'
seo_keywords: [python math module, math ceil, import math]
hints:
  - Change the number in the final call, not the metres-per-box calculation.
---

A row of floor tiles needs enough boxes to cover its full length. Each box covers four metres; an eleven-metre row needs three boxes because two would leave part of the row uncovered.

Python's standard library includes the `math` module. `import math` makes it available, and the dot in `math.ceil(...)` selects its `ceil` function. `ceil` rounds a number up to the next whole number, so `math.ceil(11 / 4)` is `3`. The starter already imports the module and defines the calculation.

## Your Task

1. Change the final `boxes_needed` call in `main.py` from `8` to `11` metres.

Press **Run** to see the result change from `2` to `3`, then **Submit**.
