---
title: "Order a stall leaderboard"
slug: sort-and-top-rows
order: 11
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Sort all rows and pick the largest values with nlargest."
seo_title: "Order a stall leaderboard | Introduction to Pandas"
seo_description: "Sort all rows and pick the largest values with nlargest."
seo_keywords: [pandas, python, data selection]
---

The notice board can show every stall in descending sales order with `sort_values("sales", ascending=False)`. When only a few leaders fit, `nlargest(2, "sales")` returns the top two without sorting the entire displayed table. Both return new tables; neither changes `sales` in place.

The starter already computes `top_two`. Change the sort direction for `result` from ascending to descending.

## Your Tasks

1. Sort `result` by sales from highest to lowest.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
