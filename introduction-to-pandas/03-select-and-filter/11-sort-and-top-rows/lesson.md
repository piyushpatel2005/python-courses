---
title: Order a stall leaderboard
slug: sort-and-top-rows
order: 11
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Sort all rows and pick the largest values with nlargest.
seo_title: Order a stall leaderboard | Introduction to Pandas
seo_description: Sort all rows and pick the largest values with nlargest.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - False switches ascending order to descending order.
---

The notice board needs the highest sales first. `sort_values("sales", ascending=False)` returns every row in descending sales order. Row labels travel with their rows; they are not new ranking numbers.

For a shorter list, `nlargest(2, "sales")` returns up to two rows with the largest numeric sales values. It keeps full rows, not just the sales column. Both calls return results without changing the supplied table.

The starter already prints top_two. Change only the direction used for result. Run should show Bee, Oak, Fern in the full ranking, then Bee and Oak in the short list.

## Your Tasks

1. Sort `result` by sales from highest to lowest.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
