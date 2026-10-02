---
title: 'Demo: Summarize Beacon Finds'
slug: demo-library-summary
order: 7
language: python
lesson_type: coding
runtime: pyodide
summary: 'Combine map records, dictionary counts, and distinct locations.'
seo_title: 'Demo: Summarize Beacon Finds | Python Basics'
seo_description: 'Combine map records, dictionary counts, and distinct locations.'
seo_keywords:
- python collections-project
- beginner collections-project exercise
---

Ari’s finds are a list of dictionaries. Each record has a `location` and a `beacon`; the same location can appear twice. A loop collects locations, `.get(beacon, 0) + 1` counts finds by beacon, and a set counts distinct locations.

Edit `main.py`, **Run** to see `2 locations` instead of `3`, then **Submit**. The next mission uses new treasure records.

## Your Task

1. Set `places` to the number of distinct values in `locations`.
