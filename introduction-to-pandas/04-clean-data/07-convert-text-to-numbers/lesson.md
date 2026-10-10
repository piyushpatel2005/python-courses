---
title: Turn text counts into numbers
slug: convert-text-to-numbers
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Coerce invalid numeric text and choose an explicit integer fallback.
seo_title: Turn text counts into numbers | Introduction to Pandas
seo_description: Coerce invalid numeric text and choose an explicit integer fallback.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - Change fillna(-1) to fillna(0); keep conversion before the fill.
---

The ticket sheet contains text: "12", "oops", and "9". Text that looks numeric still needs conversion before arithmetic. `pd.to_numeric(..., errors="coerce")` turns valid numeric text into numbers and invalid text into missing values. It does not silently turn bad text into zero.

For this report, the desk explicitly chooses zero for missing counts. `.fillna(0)` applies that rule before `.astype(int)` stores ordinary integers. Ordinary integer columns cannot hold missing values; the nullable "Int64" dtype, used next, can. These count examples contain whole numbers, not fractions to round.

Change the supplied fallback from -1 to 0. Run should print 12, 0, 9. The sequence matters: convert, choose a missing-value rule, then choose the dtype.

## Your Tasks

1. Use 0 as the fallback for invalid counts before converting to integers.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
