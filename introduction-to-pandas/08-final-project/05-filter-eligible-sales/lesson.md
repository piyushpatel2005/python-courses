---
title: Filter eligible sales
slug: filter-eligible-sales
order: 5
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Keep sales matching a channel and minimum revenue threshold.
seo_title: Filter eligible sales | Introduction to Pandas
seo_description: Keep sales matching a channel and minimum revenue threshold.
seo_keywords:
- pandas
- community market report
- boolean filter
- threshold
hints:
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Filter eligible sales

The report should be adjustable: the coordinator may want Walk-in sales today and Preorders tomorrow. Select rows whose `channel` equals a supplied string and whose `revenue` meets a supplied minimum **inclusively**. Return a copy with tidy row numbers so later steps can safely join it.

The import, clean, and enrich steps above are inherited, not tasks to repeat. Implement `select_sales`, Run with Walk-in and 4, then Submit; the tests change both arguments and include an empty selection.

## Your Tasks

1. Implement `select_sales(enriched, channel, min_revenue)` to return a reset-index copy of rows matching that channel with `revenue >= min_revenue`, leaving its input unchanged.
