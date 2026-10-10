---
title: 'Exercise: Summarize zone receipts'
slug: exercise-zone-metrics
order: 2
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Calculate separate grouped means, sums, known counts, and row counts."
seo_title: 'Exercise: Summarize zone receipts | Introduction to Pandas'
seo_description: "Calculate separate grouped means, sums, known counts, and row counts."
seo_keywords:
  - pandas
  - exercise zone metrics
  - community market data
hints:
  - 'Replace one tuple slot at a time; leave unfinished slots runnable.'
---

# Exercise: Summarize zone receipts

A new week has receipts for Pier and Hill. Calculate four separate Series so the desk can distinguish a typical known receipt from a total, a count of known amounts, and a count of rows.

Inside the function, `g = a.groupby("zone", observed=True, dropna=True)["amount"]` prepares the groups once. Calling `g.mean()`, for example, returns a Series indexed by zone. The supplied return tuple has four slots; replace them one at a time in the task order.

Pier has one known amount of 8 and one missing amount: its mean and sum are 8, its count is 1, and its size is 2. For a group whose amounts are all missing, the default sum is 0, the mean is missing, and the count is 0. That zero sum does not prove a recorded zero receipt.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Return the grouped amount mean in the first tuple slot.
2. Return the grouped amount sum in the second tuple slot.
3. Return the grouped amount count in the third tuple slot.
4. Return the grouped amount size in the fourth tuple slot.
