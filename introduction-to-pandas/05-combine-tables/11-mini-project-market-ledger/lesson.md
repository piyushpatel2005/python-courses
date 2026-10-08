---
title: 'Mini project: Assemble the market ledger'
slug: mini-project-market-ledger
order: 11
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Two delivery shifts must become one priced ledger.
seo_title: 'Mini project: Assemble the market ledger | Introduction to Pandas'
seo_description: Two delivery shifts must become one priced ledger.
seo_keywords:
- pandas
- market report
- data analysis
---

# Mini project: Assemble the market ledger

Two delivery shifts must become one priced ledger. Keep missing prices visible, reject duplicate price keys, and count unpriced rows for follow-up.

Edit `main.py`, press **Run** to inspect the current report, then **Submit** after each checkpoint.

## Your Tasks

1. Write `stack_deliveries(a, b)` to concatenate rows with a fresh index.
2. Write `add_prices(a, b)` to left-merge on `product`, validating many deliveries to one price.
3. Write `unpriced_count(ledger)` to count missing cells in the `price` column.
