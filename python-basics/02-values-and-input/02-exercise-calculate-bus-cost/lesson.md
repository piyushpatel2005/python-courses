---
title: "Exercise: Price a Cache Route"
slug: exercise-calculate-bus-cost
order: 2
language: python
lesson_type: coding
summary: "Multiply energy cost and subtract used pack slots."
seo_title: "Exercise: Price a Cache Route | Python Basics"
seo_description: "Multiply energy cost and subtract used pack slots."
seo_keywords: [python basics, values and input, lantern atlas]
---

Plan the cost and storage for a cache route. There are seven caches, with three points to collect in each. Each point costs four energy and occupies one pack slot; the pack has 25 slots.

The starter supplies those values and prints your two results. In **main.py**, replace the two zero placeholders with calculations that use the named variables. Do not type the final totals directly: the calculations should still make sense if a supplied value changes.

Press **Run** to check for `Energy cost: 84` and `Open slots: 4`, then **Submit**.

## Your Tasks

1. Calculate `energy_cost` by multiplying `points_per_cache`, `caches`, and `energy_per_point`.
2. Calculate `open_slots` by subtracting the collected points (`points_per_cache` multiplied by `caches`) from `pack_slots`.
