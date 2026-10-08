---
title: Assemble the market report
slug: assemble-market-report
order: 10
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Connect import, cleaning, enrichment, filtering, joining, grouping and CSV
  export.
seo_title: Assemble the market report | Introduction to Pandas
seo_description: Connect import, cleaning, enrichment, filtering, joining, grouping
  and CSV export.
seo_keywords:
- pandas
- community market report
- end-to-end report
- pipeline
hints:
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Assemble the market report

Every project stage now has one job. Connect them in order so a coordinator can call one function with two CSV strings, a channel, and a revenue threshold. The report still returns CSV **text**, not a saved file. The audit helper above remains available when the coordinator needs to inspect joined rows.

Edit only `build_report` at the bottom of `main.py`. Run: on the sample, Walk-in sales of at least 4 should produce North `3,7.5` and South `4,16.0`. Submit to check fresh sales and stall directories, including a different channel and threshold.

## Your Tasks

1. Implement `build_report(sales_text, stalls_text, channel, min_revenue)` using the existing functions in sequence: import → clean → enrich → select → attach → group → export. Return the final CSV string.
