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
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Exercise: compare two channels

The market coordinator asks one final review question: how much revenue came from Walk-ins versus Preorders, after the same minimum sale threshold? The `build_report` function above already handles each channel and returns CSV text. Call it for each channel, read its results with `pd.read_csv(StringIO(...))`, then add each report's `revenue` column. A channel with no qualifying sales should total zero.

This starter includes **every earlier completed market function**. Write only the new `compare_channels` function. Run to see the sample comparison, then Submit on different sales and a higher threshold. When the values match, the community market report is ready to share as CSV text.

## Your Tasks

1. Implement `compare_channels(sales_text, stalls_text, min_revenue)` to return a dictionary with exactly `Walk-in` and `Preorder` keys, each holding the total revenue from that channel's `build_report` output.
