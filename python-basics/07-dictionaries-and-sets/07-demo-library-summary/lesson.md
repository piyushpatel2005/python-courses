---
title: 'Demo: Summarize Library Visits'
slug: demo-library-summary
order: 7
language: python
lesson_type: coding
runtime: pyodide
summary: Combine a list of records, dictionary counts, and unique names.
seo_title: 'Demo: Summarize Library Visits | Python Basics'
seo_description: Combine a list of records, dictionary counts, and unique names with
  an editable Python example and checked task.
seo_keywords:
- python collections-project
- beginner collections-project exercise
---

The library logs visits as a list of dictionaries. Each record has a `name` and `room`; duplicate names represent repeat visits. Read fields by key in a loop, use `counts.get(room, 0) + 1` to count visits, and use `set(names)` for distinct people. This integrates the earlier dictionary and set lessons in a runnable project.

This is an editable worked demo. Edit `main.py`, press **Run** to compare the result, then **Submit** to check your small change. The next lesson transfers the idea to a different setting.

Change the final `people` value to count unique names instead of all visits. Run should print `2 visitors`; then Submit.

## Your Task

1. Set `people` to the count of distinct names in `names`.
