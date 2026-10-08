---
title: "Standardize names and column labels"
slug: tidy-text-and-labels
order: 9
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Strip and lowercase names, rename a field, and replace category codes."
seo_title: "Standardize names and column labels | Introduction to Pandas"
seo_description: "Strip and lowercase names, rename a field, and replace category codes."
seo_keywords: [pandas, python, data cleaning]
---

Two sellers typed the same category with inconsistent spaces or capital letters. `.str.strip().str.lower()` cleans each non-missing text value. `rename(columns={"vendor_name": "vendor"})` changes a header; `replace({"veg": "produce"})` changes a category value. A renamed column and a replaced value are different operations.

The starter already renames and replaces, but it capitalizes vendor names after stripping them. Change just `.str.upper()` to `.str.lower()`.

## Your Tasks

1. Store stripped, lowercase vendor names in `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
