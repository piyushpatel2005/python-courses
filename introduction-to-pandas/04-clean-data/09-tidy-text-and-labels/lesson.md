---
title: Standardize names and column labels
slug: tidy-text-and-labels
order: 9
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Strip and lowercase names, rename a field, and replace category codes.
seo_title: Standardize names and column labels | Introduction to Pandas
seo_description: Strip and lowercase names, rename a field, and replace category codes.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - Keep strip() and change the following str.upper() call to str.lower().
---

The vendor names contain padding and inconsistent capitals. `.str.strip()` removes whitespace at the ends of each text value; `.str.lower()` lowercases it. The `.str` accessor applies string operations across a Series, and missing entries stay missing.

The starter also performs two different edits. `rename(columns={"vendor_name": "vendor"})` changes a header. `.replace({"veg": "produce"})` changes exact category values, not the header. Neither operation cleans the other column automatically.

Only the final case choice for vendor names needs changing. Replace upper with lower. Run should show mina and sol under vendor, with produce and bread still in the category column.

## Your Tasks

1. Store stripped, lowercase vendor names in `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
