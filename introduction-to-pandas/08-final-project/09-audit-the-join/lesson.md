---
title: Audit the reported rows
slug: audit-the-join
order: 9
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Count included sales, unmatched stalls and revenue before sharing.
seo_title: Audit the reported rows | Introduction to Pandas
seo_description: Count included sales, unmatched stalls and revenue before sharing.
seo_keywords:
- pandas
- community market report
- audit
- missing join
hints:
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Audit the reported rows

A report may still include a sale whose stall is missing from the directory. Before sharing it, show the coordinator a concise audit: how many selected rows were joined, how many have no `stall_name`, and the total revenue of those rows. The audit must be based on the joined rows rather than the raw sales sheet, because filtering has already changed the scope.

All previous project functions remain complete. Implement only `audit_sales`, Run to inspect the dictionary, then Submit on altered joined rows.

## Your Tasks

1. Implement `audit_sales(joined)` to return `{"rows": row_count, "unmatched": missing_stall_name_count, "revenue": summed_revenue}` for the supplied joined DataFrame.
