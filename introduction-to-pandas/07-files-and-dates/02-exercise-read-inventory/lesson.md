---
title: 'Exercise: load inventory CSV'
slug: exercise-read-inventory
order: 2
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Write a reusable function that reads changing inventory CSV text.
seo_title: 'Exercise: load inventory CSV | Introduction to Pandas'
seo_description: Write a reusable function that reads changing inventory CSV text.
seo_keywords:
- pandas
- read_csv
- inventory CSV
hints:
- Use the example above the task and check the printed result before submitting.
---

# Exercise: load inventory CSV

The supply desk has a different sheet: `item,stock` rather than `stall,visits`. Reuse the buffer pattern from the preceding lesson, but write a new function rather than copying a fixed table.

Edit `main.py`. Run to inspect the loaded inventory, then Submit. Your function must use its **text parameter**, including when the sheet has only one row.

## Your Tasks

1. Implement `load_inventory(text)` to return a DataFrame with `item` and numeric `stock` columns parsed from the supplied CSV text.
