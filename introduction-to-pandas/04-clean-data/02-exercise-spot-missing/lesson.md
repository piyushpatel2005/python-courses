---
title: 'Exercise: audit delivery addresses'
slug: exercise-spot-missing
order: 2
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Mark missing addresses and drop rows only when address is absent.
seo_title: 'Exercise: audit delivery addresses | Introduction to Pandas'
seo_description: Mark missing addresses and drop rows only when address is absent.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - Use isna on the address Series and dropna with address in subset.
---

The delivery board can tolerate a missing phone number, but it needs an address to route a parcel. Write one function to identify the gaps and another to return the usable rows. Neither function should alter the original board.

Selecting address first and calling isna gives a Boolean Series rather than a whole Boolean table. For the second function, limit dropna to that one required column. An empty string still counts as present under this rule; checking meaningful address text would need another rule.

The two Run probes are supplied. Task 1 should print False, True, False for a, b, c. Task 2 should retain D1 and D3 even though D1 has no phone.

## Your Tasks

1. Return a boolean Series showing which `address` cells are missing from `missing_addresses(frame)`.
2. Return rows with a present `address` from `routable(frame)`, keeping rows that have a missing `phone`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
