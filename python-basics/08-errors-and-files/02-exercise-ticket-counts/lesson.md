---
title: "Exercise: Recover Ticket Counts"
slug: exercise-ticket-counts
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Convert ticket quantities and handle bad input without hiding other errors.
seo_title: "Exercise: Recover Ticket Counts | Python Basics"
seo_description: Convert ticket quantities and handle bad input without hiding other errors.
seo_keywords: [python try except exercise, traceback, ValueError]
---

A ticket spreadsheet sometimes contains `"many"` instead of digits. The prior demo caught a specific conversion failure; now use it for a different function. `IndexError` from a bad list index or `NameError` from a typo would not be fixed by catching `ValueError`, so do not use a bare `except`.

Edit `main.py`, Run to compare both sample labels, then Submit. The starter supplies the labels; each helper is independently testable.

## Your Tasks

1. Complete `ticket_count(text)` to return `int(text)` for valid integer text and `0` for text that raises `ValueError`, using `try`/`except ValueError`.
2. Complete `ticket_label(text)` to return `"Tickets: <count>"` using `ticket_count(text)`.
