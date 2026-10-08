---
title: "Project: prepare a market log"
slug: exercise-clean-market-log
order: 12
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Clean a market log in seven small, testable steps."
seo_title: "Project: prepare a market log | Introduction to Pandas"
seo_description: "Clean a market log in seven small, testable steps."
seo_keywords: [pandas, python, data cleaning]
---

The market desk receives a log with padded seller names, text quantities, missing categories, and repeated visits. Build seven small functions, then read the printed pipeline. Each stage accepts a table and returns a new one, so the input stays available for auditing.

First rename `seller_name` to `seller`, tidy the names, convert `units` with invalid text coerced to missing nullable integers, and drop rows without a seller or numeric units. Next fill missing categories with `unassigned` and retain the **last** row for each `seller`/`day` pair. Finally use `.loc` on a copy to mark rows whose units reach the supplied cutoff. Keep every remaining column and original index; do not reset the index. Each function can be checked on its own, even before the whole pipeline works.

You now have a reusable cleaning pipeline for the market desk's next delivery, not just the printed result.

## Your Tasks

1. Make `rename_seller(frame)` rename `seller_name` to `seller`.
2. Make `tidy_seller(frame)` strip and lowercase the `seller` column.
3. Make `convert_units(frame)` turn `units` into nullable `Int64`, coercing invalid text to missing.
4. Make `drop_incomplete(frame)` discard rows missing either `seller` or `units`.
5. Make `fill_category(frame)` replace missing `category` with `unassigned`.
6. Make `keep_latest(frame)` retain the last record for each `seller` and `day` pair.
7. Make `mark_ready(frame, minimum)` set `status` to `ready` for rows with `units >= minimum` using `.loc` on a copy.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
