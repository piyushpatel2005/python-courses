---
title: "Recognize repeated entries"
slug: find-duplicate-rows
order: 5
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Compare duplicated masks with dropping duplicates on a chosen key."
seo_title: "Recognize repeated entries | Introduction to Pandas"
seo_description: "Compare duplicated masks with dropping duplicates on a chosen key."
seo_keywords: [pandas, python, data cleaning]
---

The same stall may check in on different days. `duplicated(subset=["stall", "day"])` flags the second occurrence of the **same pair**; `drop_duplicates` keeps the first pair by default. Looking only at `stall` would wrongly remove a later day's visit.

The starter removes every later visit for a stall. Add `"day"` to the subset list in `result` so only repeat visits on the same day disappear.

## Your Tasks

1. Deduplicate by both `stall` and `day` in `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
