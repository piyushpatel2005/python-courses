---
title: "Exercise: shortlist ready orders"
slug: exercise-comparison-masks
order: 6
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Filter orders by a minimum quantity without losing row labels."
seo_title: "Exercise: shortlist ready orders | Introduction to Pandas"
seo_description: "Filter orders by a minimum quantity without losing row labels."
seo_keywords: [pandas, python, data selection]
---

The order desk needs a shortlist before pickup. Use the comparison-mask pattern on `quantity`, not the example's `crates`. Include orders exactly at the minimum.

## Your Tasks

1. Return every row with `quantity` at least `minimum` from `ready_orders(frame, minimum)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
