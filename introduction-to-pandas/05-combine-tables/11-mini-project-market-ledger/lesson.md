---
title: 'Mini project: Assemble the market ledger'
slug: mini-project-market-ledger
order: 11
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Assemble delivery rows, validate price matches, and count unpriced entries."
seo_title: 'Mini project: Assemble the market ledger | Introduction to Pandas'
seo_description: "Assemble delivery rows, validate price matches, and count unpriced entries."
seo_keywords:
  - pandas
  - market report
  - data analysis
hints:
  - 'Use many_to_one for the price lookup, and count missing prices rather than missing products.'
---

# Mini project: Assemble the market ledger

The Community Data Desk is ready to assemble a delivery ledger. Stack the two shifts, attach the product prices, then count the rows that still need a price. Keep the missing prices visible rather than replacing them with zero.

Each function has its own input and can be checked independently. `add_prices` must work on any supplied delivery table, even before your stacking function is finished. For the final count, select `price`, use `isna()` to mark missing cells, and sum that Boolean Series; each `True` contributes one.

The completed preview has Tea and Jam, with one unpriced row for Jam. This finishes the table-combining work; next you will turn records into group summaries.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Write `stack_deliveries(a, b)` to concatenate rows with a fresh index.
2. Write `add_prices(a, b)` to left-merge on `product`, validating many deliveries to one price.
3. Write `unpriced_count(ledger)` to count missing cells in the `price` column.
