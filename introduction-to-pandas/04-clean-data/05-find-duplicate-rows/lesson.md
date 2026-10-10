---
title: Recognize repeated entries
slug: find-duplicate-rows
order: 5
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Compare duplicated masks with dropping duplicates on a chosen key.
seo_title: Recognize repeated entries | Introduction to Pandas
seo_description: Compare duplicated masks with dropping duplicates on a chosen key.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - The subset list needs both parts of the visit key.
---

Bee can visit on both Friday and Saturday. A repeated stall name alone does not make a repeated visit. Here the visit key is the pair of values in stall and day.

`duplicated(subset=["stall", "day"])` returns a mask that marks each later occurrence of that pair True. By default, the first occurrence is False. `drop_duplicates` uses the same key to keep the first row and remove later occurrences. The note and row index do not participate in this comparison.

The starter's mask already uses the pair, but result only uses stall. Add day to that subset. Run should print False, False, True, then retain Friday's first visit and Saturday's visit.

## Your Tasks

1. Deduplicate by both `stall` and `day` in `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
