---
title: "Exercise: audit delivery addresses"
slug: exercise-spot-missing
order: 2
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Mark missing addresses and drop rows only when address is absent."
seo_title: "Exercise: audit delivery addresses | Introduction to Pandas"
seo_description: "Mark missing addresses and drop rows only when address is absent."
seo_keywords: [pandas, python, data cleaning]
---

A delivery board cannot route a package without an address, but a missing phone number is acceptable. First identify the missing `address` cells, then return a delivery table that requires that field. Accept different row labels and records.

## Your Tasks

1. Return a boolean Series showing which `address` cells are missing from `missing_addresses(frame)`.
2. Return rows with a present `address` from `routable(frame)`, keeping rows that have a missing `phone`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
