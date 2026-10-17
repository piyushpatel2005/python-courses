---
title: 'Demo: Inventory the neighborhood tables'
slug: demo-inventory-three-tables
order: 1
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Preview a garden trend from three small, named DataFrames.'
seo_title: 'Demo: Inventory the neighborhood tables | Introduction to Matplotlib'
seo_description: 'Preview a garden trend from three small, named DataFrames.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'demo'
  - 'inventory'
  - 'the'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Demo: Inventory the neighborhood tables

The final dashboard will bring together garden temperature, library visits, and transit rides. Each table has a `day` column, but the other columns mean different things. Start with a garden line: it preserves day order and uses degrees Celsius rather than an unlabeled number. Change the title to make the unit explicit; the other two tables are waiting for later lessons.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Set the garden title to `Garden temperature (°C)`.
