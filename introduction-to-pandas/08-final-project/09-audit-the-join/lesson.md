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
  - "Use joined[\"stall_name\"].isna().sum() for unmatched and joined[\"revenue\"].sum() for the total."
---

# Audit the reported rows

Before sharing the report, give the coordinator a small audit of the joined sales. Count the included rows, count missing stall names, and total the revenue across all those rows. Work from `joined`, not the raw sheet: cleaning and filtering have already changed which sales qualify.

`len(joined)` counts rows. For missing names, `.isna()` creates a boolean Series and `.sum()` counts its True values. Here `unmatched` means a missing `stall_name`; a directory row with a blank name would count too, so it is a useful flag for inspection rather than proof of a failed match.

Edit `audit_sales` in `main.py`. The dictionary and return are supplied; add one key at each task comment. Run works with a partly filled dictionary. Submit checks each key independently, including an empty joined table.

The sample audit should read `{"rows": 2, "unmatched": 0, "revenue": 23.5}`. Revenue includes all selected joined rows, not only those with missing names.

## Your Tasks

1. Add a `rows` entry holding the number of joined rows.
2. Add an `unmatched` entry holding the number of missing `stall_name` values.
3. Add a `revenue` entry holding the sum of the joined `revenue` column.
