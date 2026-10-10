---
title: Spot missing records before filing
slug: spot-missing-cells
order: 1
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Use isna to see missing cells and dropna subset to require one field.
seo_title: Spot missing records before filing | Introduction to Pandas
seo_description: Use isna to see missing cells and dropna subset to require one field.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - The subset list names required fields, not fields to remove.
---

A row can exist even when one of its cells is missing. Before sending the contact list, the desk needs to distinguish a missing email from a missing optional note.

`signups.isna()` returns a table of Boolean decisions with the same shape. True means missing. Pandas recognizes markers such as None, NaN, and pd.NA; use isna rather than equality to test them. A blank string, "", is text and is not automatically missing. The way a missing cell prints can vary with its column dtype.

`dropna(subset=["email"])` returns rows where email is present. It does not require a note, or check whether an email is valid. Change the starter's subset from note to email. Run should retain Ada and Cy; Ada's missing note is allowed.

![A three-row table marks missing cells; only rows missing the required email are removed.](missing-data-flow.svg)

## Your Tasks

1. Require a non-missing `email` when creating `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
