---
title: 'Exercise: compare two channels'
slug: exercise-compare-channels
order: 11
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Reuse the finished report pipeline to compare two channel totals.
seo_title: 'Exercise: compare two channels | Introduction to Pandas'
seo_description: Reuse the finished report pipeline to compare two channel totals.
seo_keywords:
  - pandas
  - community market report
  - review exercise
  - channel comparison
hints:
  - "Loop over (\"Walk-in\", \"Preorder\"), call build_report for each, and read its text before summing revenue."
---

# Exercise: compare two channels

The coordinator's last question is a comparison: how much qualifying revenue came from Walk-ins and how much from Preorders? The same minimum sale threshold must apply to both.

`build_report` already does the filtering and reporting. Call it once for each channel, read each returned CSV string through `StringIO`, and sum that report's `revenue` column. An empty report still has headers; its revenue sum is zero. Reusing the report also keeps unknown neighborhoods in the comparison instead of losing their sales.

All earlier functions are complete in `main.py`. Implement only `compare_channels`, then Run with the supplied threshold of 4. The result should be `{"Walk-in": 23.5, "Preorder": 8.0}`. Submit checks new sheets and a threshold high enough to exclude every sale.

## Your Tasks

1. Implement `compare_channels(sales_text, stalls_text, min_revenue)` to return exactly the `Walk-in` and `Preorder` keys, each holding the summed revenue from that channel's `build_report` output.

You now have a reusable report for the Community Data Desk: new input strings and selection arguments can produce a new CSV without rewriting the cleaning steps.
