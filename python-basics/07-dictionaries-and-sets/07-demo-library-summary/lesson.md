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

Each find is a dictionary with a `location` and a `beacon`. The list keeps all the finds, including repeated visits to one location.

Read the supplied loop in `main.py`. It collects locations and counts each beacon with `.get(beacon, 0) + 1`. For a new beacon, `get()` returns zero and the count becomes one. When that beacon appears again, its stored count of one becomes two.

The last calculation counts visits rather than distinct places. Change it to count unique locations. Run should show `2 locations` instead of `3`, then Submit.

## Your Task

1. Set `places` to the number of distinct values in `locations`.
