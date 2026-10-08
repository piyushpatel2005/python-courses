---
title: "Combine two selection rules"
slug: combine-masks
order: 7
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Use parenthesized comparisons with and/or masks."
seo_title: "Combine two selection rules | Introduction to Pandas"
seo_description: "Use parenthesized comparisons with and/or masks."
seo_keywords: [pandas, python, data selection]
---

The desk checks whether a stall both has enough baskets **and** sits in the east aisle. Each comparison needs parentheses: `(table["baskets"] >= 4) & (table["aisle"] == "east")`. Use `&` for both and `|` for either; ordinary Python `and`/`or` do not compare row by row.

The starter uses `|`, so it admits stalls meeting just one rule. Change that one operator to `&`.

## Your Tasks

1. Require both conditions by replacing the operator in `mask` with `&`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
