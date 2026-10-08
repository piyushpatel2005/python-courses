---
title: Merge on a named key
slug: merge-on-stall
order: 5
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Some bookings have no vendor record yet.
seo_title: Merge on a named key | Introduction to Pandas
seo_description: Some bookings have no vendor record yet.
seo_keywords:
- pandas
- merge on stall
- community market data
---

# Merge on a named key

Some bookings have no vendor record yet. An inner merge keeps only matched keys; a left merge retains every booking. Unlike column concatenation, merge compares values in a named column.

![Inner and left merges match values in stall keys](merge-key.svg)

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Change `how="inner"` to `how="left"` in `attach_vendors`.
