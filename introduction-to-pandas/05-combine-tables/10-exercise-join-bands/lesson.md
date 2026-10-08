---
title: 'Exercise: Join fee bands'
slug: exercise-join-bands
order: 10
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: A fresh booking ledger needs an indexed fee lookup.
seo_title: 'Exercise: Join fee bands | Introduction to Pandas'
seo_description: A fresh booking ledger needs an indexed fee lookup.
seo_keywords:
- pandas
- exercise join bands
- community market data
---

# Exercise: Join fee bands

A fresh booking ledger needs an indexed fee lookup. A repeated lookup index could inflate the result: check uniqueness first, then retain unmatched bookings.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Complete `attach_bands(a, b)` by rejecting a nonunique lookup index with `ValueError`, then left-joining `b` after setting `band` as the left index.
