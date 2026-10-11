---
title: Update selected rows safely
slug: assign-with-loc
order: 11
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Copy a table and assign to rows and a column together with loc.
seo_title: Update selected rows safely | Introduction to Pandas
seo_description: Copy a table and assign to rows and a column together with loc.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - Keep the mask and status column in the same loc assignment; change its assigned string.
---

The supply desk wants to mark low-stock items while preserving its original record. `cleaned = stock.copy()` creates the table you will edit. The assignment must target cleaned itself.

`cleaned.loc[cleaned["units"] < 3, "status"] = "review"` gives Pandas the row mask and target column together. Only the cells at that intersection change. Rows with three or more units keep their existing status, and stock is untouched.

Do not split the update into selections such as `cleaned[mask]["status"] = ...`. That chained assignment targets a temporary selection, not the intended table; with Pandas 3 Copy-on-Write it does not update cleaned. The single loc assignment works across the versions used by this course.

Change the supplied value watch to review. Run should show Beans and Rice marked review while Tea stays ok.

![A copy keeps all stock rows; a row mask and the status column select only the two cells changed to review.](safe-loc-update.svg)

## Your Tasks

1. Mark low-stock rows as `review` using the existing `.loc` assignment.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
