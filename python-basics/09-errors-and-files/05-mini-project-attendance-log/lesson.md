---
title: 'Mini project: Save an attendance total'
slug: mini-project-attendance-log
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: 'Handle invalid headcounts and save an attendance total.'
seo_title: 'Mini project: Save an attendance total | Python Basics'
seo_description: 'Handle invalid headcounts and save an attendance total.'
seo_keywords: [python mini project, ValueError, file handling]
---

You have headcounts recorded as text for several check-ins. Some entries may be mistyped. Add the valid counts, treat invalid integer text as zero, then write one line to `attendance-log.txt` and read it back.

The list is supplied; you do not need `input()`. For example, `"2"`, `"unknown"`, and `"3"` produce a total of `5`. A `try`/`except ValueError` inside the loop keeps one bad entry from stopping the rest. Use the total in the saved line rather than writing a fixed result. The file is temporary in this browser exercise, not a permanent download.

## Your Tasks

1. Complete `total_attendance(entries)` to add converted values in a loop, treating `ValueError` entries as zero; an empty list totals zero.
2. Complete `save_attendance(entries)` to write exactly `"Attendees: <total>"` to `attendance-log.txt` using `total_attendance` and `with open(..., "w", encoding="utf-8")`.
3. Complete `read_attendance()` to return the whole saved file using `with open(..., "r", encoding="utf-8")`.

Edit `main.py` and **Submit** after each helper. When all three work, **Run** prints `Attendees: 5`. Before that, an unfinished helper may print `None`.
