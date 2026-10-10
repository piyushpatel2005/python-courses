---
title: Combine two selection rules
slug: combine-masks
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Combine parenthesized comparisons with & and | masks.
seo_title: Combine two selection rules | Introduction to Pandas
seo_description: Combine parenthesized comparisons with & and | masks.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - Keep both parenthesized comparisons and change only the operator between them.
---

A stall must have enough baskets and be in the east aisle. Each rule produces a mask; combine the decisions for the same row. `&` means both decisions must be True. `|` means at least one may be True, including when both are.

Write each comparison in parentheses before combining them. For example, `(table["baskets"] >= 4) & (table["aisle"] == "east")`. Python's ordinary `and` and `or` expect one truth value, not a Series of row decisions.

The starter uses `|`, so all three stalls pass one rule or the other. Change just the operator. Run should then show Fern alone: Bee has too few baskets and Oak is in the west aisle.

## Your Tasks

1. Require both conditions by replacing the operator in `mask` with `&`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
