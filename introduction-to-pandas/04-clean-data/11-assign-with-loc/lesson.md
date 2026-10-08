---
title: "Update selected rows safely"
slug: assign-with-loc
order: 11
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Copy a table and assign to rows and a column together with loc."
seo_title: "Update selected rows safely | Introduction to Pandas"
seo_description: "Copy a table and assign to rows and a column together with loc."
seo_keywords: [pandas, python, data cleaning]
---

The supply desk marks low-stock items for review. First `copy()` the table so the incoming records remain untouched. Then `cleaned.loc[cleaned["units"] < limit, "status"] = "review"` selects rows and a column in one assignment. Avoid assigning into a filtered temporary table; that may not update the table you meant to change.

The starter uses `"watch"` for low stock. Change that one assigned value to `"review"`.

## Your Tasks

1. Mark low-stock rows as `review` using the existing `.loc` assignment.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
