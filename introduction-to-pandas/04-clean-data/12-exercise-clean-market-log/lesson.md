---
title: 'Project: prepare a market log'
slug: exercise-clean-market-log
order: 12
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Clean a market log in seven small, testable steps.
seo_title: 'Project: prepare a market log | Introduction to Pandas'
seo_description: Clean a market log in seven small, testable steps.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - Work through the functions in order; keep a copy before replacing a column or assigning with loc.
---

The desk receives a log with padded seller names, text quantities, missing categories, and repeated visits. Build a small cleaning pipeline without overwriting that raw record. Each function accepts a table and returns a new one; the supplied print code connects them.

Order matters. Rename the seller header before selecting it. Clean names before comparing seller/day pairs, or MINA and Mina would count as different sellers. Convert units before dropping missing numbers, or "unknown" would still be ordinary text. For this log, valid counts are whole numbers.

After removing rows missing seller or units, fill only missing categories. Keep the last occurrence of each seller/day pair; input order represents revision order here, not sorted date order. Finally mark qualifying rows ready with one loc assignment on a copy. Leave other statuses, columns, and row labels alone. Empty text is not automatically missing.

Each function is checked separately on suitable input, so task 1 can pass before task 2 is written. The supplied Run pipeline waits for the seller header and numeric units before using them. At the end it should show only revised: seller mina, units 7, category veg, status ready. The raw first row is superseded and the unusable row has no numeric units.

This gives the desk a cleaned table ready for the next section, where separate tables will be combined.

## Your Tasks

1. Make `rename_seller(frame)` rename `seller_name` to `seller`.
2. Make `tidy_seller(frame)` strip and lowercase the `seller` column.
3. Make `convert_units(frame)` turn `units` into nullable `Int64`, coercing invalid text to missing.
4. Make `drop_incomplete(frame)` discard rows missing either `seller` or `units`.
5. Make `fill_category(frame)` replace missing `category` with `unassigned`.
6. Make `keep_latest(frame)` retain the last record for each `seller` and `day` pair.
7. Make `mark_ready(frame, minimum)` set `status` to `ready` for rows with `units >= minimum` using `.loc` on a copy.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
