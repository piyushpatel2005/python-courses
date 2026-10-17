---
title: "Exercise: Price a Cache Route"
slug: exercise-calculate-bus-cost
order: 3
language: python
lesson_type: coding
summary: "Multiply energy cost and subtract used pack slots."
seo_title: "Exercise: Price a Cache Route | Python Basics"
seo_description: "Multiply energy cost and subtract used pack slots."
seo_keywords: [python basics, values and input, lantern atlas]
---

In this lesson, you will plan the cost and storage for a cache route. There are seven treasure chests, with three coins to collect in each. Each coin costs four points and occupies one pack slot; the pack has 25 slots.

The starter supplies those values and prints your two results. In **main.py**, replace the two zero placeholders with calculations that use the named variables. Do not type the final totals directly: the calculations should still make sense if a supplied value changes.

Press **Run** to check for `Points needed: 84` and `Open slots: 4`, then **Submit**.

## Your Tasks

1. Calculate `points_needed` by multiplying `coins_per_chest`, `number_of_chests`, and `points_per_coin`.
2. Calculate `open_slots` by subtracting the collected points (`coins_per_chest` multiplied by `number_of_chests`) from `pack_slots`.
