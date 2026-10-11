---
title: 'Exercise: Join fee bands'
slug: exercise-join-bands
order: 10
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Join fee bands by index and reject repeated lookup labels."
seo_title: 'Exercise: Join fee bands | Introduction to Pandas'
seo_description: "Join fee bands by index and reject repeated lookup labels."
seo_keywords:
  - pandas
  - exercise join bands
  - community market data
hints:
  - 'Put the uniqueness guard before the return so duplicate lookups never reach the join.'
---

# Exercise: Join fee bands

A booking ledger needs fees from a lookup indexed by band. Build the normal join first, then add a guard against repeated lookup labels. These are separate checks, so you can submit after either step.

`b.index.is_unique` is a Boolean: it is `True` only when no index label repeats. Before the join, use `if not b.index.is_unique:` followed by `raise ValueError("Duplicate fee-band keys")`. Raising an error stops this function instead of returning misleading rows. The error message can be your own.

For a valid lookup, set the left index to `band` and use a left join. The supplied A booking gets fee 5; B stays present with a missing fee.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Make `attach_bands(a, b)` return a left join of `b` onto `a`, using `band` as the left index.
2. Reject a repeated lookup index by raising `ValueError` before joining.
