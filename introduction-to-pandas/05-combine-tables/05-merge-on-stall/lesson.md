---
title: Merge on a named key
slug: merge-on-stall
order: 5
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Choose which booking keys survive an inner or left merge."
seo_title: Merge on a named key | Introduction to Pandas
seo_description: "Choose which booking keys survive an inner or left merge."
seo_keywords:
  - pandas
  - merge on stall
  - community market data
hints:
  - 'The how argument controls which keys survive; on names the column to match.'
---

# Merge on a named key

The booking sheet stores stall names in a column rather than in its index. A **key** is the value used to find the corresponding record in another table. Here `on="stall"` tells `merge` which column holds that key; `a` is the left table and `b` is the right table.

The starter uses an inner merge, which keeps only keys found on both sides. A left merge keeps every booking and adds vendor information where it exists. After the change, Lark still has Ari as its vendor, and Unknown remains with missing vendor information. A right merge keeps the right-side keys; an outer merge keeps keys from either side.

These lookup keys are unique. Repeated matches can create extra rows, which we will check in the next pair of lessons. Also, pandas can match missing keys to each other: clean or investigate missing identifiers before merging. A missing vendor is not evidence that the booking itself is invalid.

![Inner, left, right, and outer merges keep different sets of stall keys](merge-key.svg)

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Change `how="inner"` to `how="left"` in `attach_vendors`.

## Learn more

The pandas [merge documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) gives the full argument details and more examples.
