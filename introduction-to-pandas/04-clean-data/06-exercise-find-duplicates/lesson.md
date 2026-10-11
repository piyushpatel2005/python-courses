---
title: 'Exercise: reconcile order revisions'
slug: exercise-find-duplicates
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Flag and keep the last record for each order and date.
seo_title: 'Exercise: reconcile order revisions | Introduction to Pandas'
seo_description: Flag and keep the last record for each order and date.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - Use the same two-column subset and keep="last" in both functions.
---

A volunteer can revise an order more than once on the same date. In this log, revisions are already arranged in the order they arrived. The last occurrence is therefore the revision to keep. `keep="last"` does not inspect a timestamp or sort the data for you.

Use order and date together as the key. With duplicated, keep="last" marks earlier occurrences True. With drop_duplicates, it keeps the final occurrence instead. Different dates remain separate, even for the same order.

After task 1, Run should print True, False, False. After task 2, the table should retain other-day and new, including Friday's corrected count of 4 bags.

## Your Tasks

1. Return a boolean Series marking older revisions from `older_revisions(frame)`.
2. Return the latest row per `order` and `date` from `latest_revisions(frame)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
