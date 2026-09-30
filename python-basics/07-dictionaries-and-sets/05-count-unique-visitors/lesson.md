---
title: Keep Unique Visitors in a Set
slug: count-unique-visitors
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: Deduplicate names and compare Python sets.
seo_title: Keep Unique Visitors in a Set | Python Basics
seo_description: Deduplicate names and compare Python sets with an editable Python
  example and checked task.
seo_keywords:
- python sets
- beginner sets exercise
---

A set holds unique values but does not have indexes or guaranteed display order. `set(names)` removes duplicates; `seen.add(name)` adds one; `set()` creates an empty set (`{}` creates a dictionary). With two sets, `&` means overlap, `|` means union and `-` means first-only. Sort before printing a predictable order.

This is an editable worked demo. Edit `main.py`, press **Run** to compare the result, then **Submit** to check your small change. The next lesson transfers the idea to a different setting.

Change `unique` to count distinct visitors rather than copying the list; Run should print `2`; then Submit.

## Your Task

1. Set `unique` to a set of the distinct names in `visitors`.
