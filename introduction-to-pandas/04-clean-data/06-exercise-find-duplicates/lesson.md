---
title: "Exercise: reconcile order revisions"
slug: exercise-find-duplicates
order: 6
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Flag and keep the last record for each order and date."
seo_title: "Exercise: reconcile order revisions | Introduction to Pandas"
seo_description: "Flag and keep the last record for each order and date."
seo_keywords: [pandas, python, data cleaning]
---

A volunteer may correct an order on the same date, while orders on separate dates remain separate. `.duplicated(..., keep="last")` marks earlier revisions; `drop_duplicates(..., keep="last")` retains the final record for each key. Use both `order` and `date` as that key.

## Your Tasks

1. Return a boolean Series marking older revisions from `older_revisions(frame)`.
2. Return the latest row per `order` and `date` from `latest_revisions(frame)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
