---
title: Guard against duplicate prices
slug: guard-duplicate-prices
order: 7
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Repeat orders can share a product, but each product should have one price.
seo_title: Guard against duplicate prices | Introduction to Pandas
seo_description: Repeat orders can share a product, but each product should have one
  price.
seo_keywords:
- pandas
- guard duplicate prices
- community market data
---

# Guard against duplicate prices

Repeat orders can share a product, but each product should have one price. Duplicate keys on both sides multiply output rows. `validate="many_to_one"` permits repeat orders and rejects a duplicate price key; `many_to_many` does not protect you.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Change `validate` from `many_to_many` to `many_to_one`.
