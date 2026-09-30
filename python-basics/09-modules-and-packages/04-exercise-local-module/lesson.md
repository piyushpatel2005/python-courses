---
title: "Exercise: Local Module"
slug: exercise-local-module
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: Call a reusable function imported from a local module.
seo_title: "Exercise: Local Module | Python Basics"
seo_description: Call a reusable function imported from a local module.
seo_keywords: [python basics, exercise local module, python practice]
hints:
  - Use from supply_rules import box_count; then call box_count(items).
---

# Exercise: Local Module

The supplied setup writes a separate `supply_rules.py` module into the browser filesystem. Its `box_count` function rounds up packs of four; you do not need to write or install the module. Import it into `main.py` and use it in your own function. In a regular project the helper would live as a neighboring `.py` file rather than being generated at run time.

## Your Tasks

1. Import `box_count` from `supply_rules` after the supplied setup.
2. Complete `order_boxes(items)` to return the imported helper’s result for `items`.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.
