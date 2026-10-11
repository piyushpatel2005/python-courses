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
  - "Combine (enriched[\"channel\"] == channel) and (enriched[\"revenue\"] >= min_revenue) with &."
---

# Filter eligible sales

The coordinator wants to choose a channel and a minimum sale value instead of getting the same report every time. Both function arguments matter: a row must match `channel` and have `revenue >= min_revenue`. The threshold is inclusive, so revenue exactly equal to the minimum stays.

The earlier functions are complete in `main.py`. Implement `select_sales` with a boolean mask; put parentheses around each comparison before joining them with `&`. Return a copy with a fresh index. That index is a presentation choice, not a requirement for merging on `stall_id` later.

Run uses `"Walk-in"` and 4. It should keep sale IDs 1 and 5; the Tea sale is below the threshold and the other Bread sale is a Preorder. Submit also checks another channel and a selection with no matching rows.

## Your Tasks

1. Implement `select_sales(enriched, channel, min_revenue)` to return a reset-index copy of rows matching that channel with `revenue >= min_revenue`, leaving the input unchanged.
