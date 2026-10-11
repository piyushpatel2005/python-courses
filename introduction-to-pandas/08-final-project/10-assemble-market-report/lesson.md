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
  - "Keep stalls from read_tables for attach_stalls; pass each other result into the next helper."
---

# Assemble the market report

Each stage is now written. Give the coordinator one function that runs them in order for new input sheets. The completed helpers stay above `build_report` in `main.py`; reuse them rather than repeating their code.

Start by unpacking `read_tables` into sales and stalls. Pass sales through cleaning, enrichment, and selection. The directory waits until `attach_stalls`, where it joins the selected rows. Then group and export. Local names for each intermediate table make it easier to inspect a stage if the result is surprising.

The audit helper remains available for inspecting joined rows, but this function returns only CSV text. Do not put the audit dictionary into the CSV or save a file.

Implement `build_report`, then Run. With Walk-in sales of at least 4, the sample produces North `3.0,7.5` and South `4.0,16.0`. Submit changes the sheets, channel, and threshold and checks that the helpers receive each other's results.

## Your Tasks

1. Implement `build_report(sales_text, stalls_text, channel, min_revenue)` by calling the supplied import → clean → enrich → select → attach → group → export functions in order, returning the final CSV string.
