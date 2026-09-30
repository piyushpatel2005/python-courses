---
title: "Mini Project: Attendance Log"
slug: mini-project-attendance-log
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: Parse counts, save a report, and read the report back.
seo_title: "Mini Project: Attendance Log | Python Basics"
seo_description: Parse counts, save a report, and read the report back.
seo_keywords: [python mini project, error handling, file handling]
---

A workshop coordinator has an arrival sheet with numeric text and occasional bad entries. Make a small report that survives long enough to be read back **within this run**. This pulls together `try`/`except`, loops, functions, f-strings, and browser file operations. The file `attendance-log.txt` is temporary in Pyodide, not on your computer; each test creates its own data and writes before reading. Use no `input()` calls.

Edit `main.py` and Run: the sample should finish with `Arrivals: 5`. Submit after each helper, in task order.

## Your Tasks

1. Complete `total_arrivals(entries)` to add converted counts in a loop; treat entries that raise `ValueError` during `int(...)` as zero. An empty list totals zero.
2. Complete `save_log(entries)` to write exactly `"Arrivals: <total>"` to `attendance-log.txt` with `with open(..., "w", encoding="utf-8")`, using `total_arrivals`.
3. Complete `read_log()` to read and return the entire `attendance-log.txt` file with `with open(..., "r", encoding="utf-8")`.

You've built a report that handles messy source values without letting one bad count stop the shift.
