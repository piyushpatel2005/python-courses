---
title: Join indexed areas
slug: join-indexed-areas
order: 9
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: The area lookup uses area codes as index labels.
seo_title: Join indexed areas | Introduction to Pandas
seo_description: The area lookup uses area codes as index labels.
seo_keywords:
- pandas
- join indexed areas
- community market data
---

# Join indexed areas

The area lookup uses area codes as index labels. Set the left table’s `area` column as its index before `join`. A left join retains stalls without a matching lookup; an inner join drops them.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Change `how` to `left` in `attach_areas`.
