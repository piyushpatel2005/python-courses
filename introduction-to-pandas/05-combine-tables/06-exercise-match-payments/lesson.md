---
title: 'Exercise: Match payments'
slug: exercise-match-payments
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Attach payment status without dropping unmatched reservations."
seo_title: 'Exercise: Match payments | Introduction to Pandas'
seo_description: "Attach payment status without dropping unmatched reservations."
seo_keywords:
  - pandas
  - exercise match payments
  - community market data
hints:
  - 'Use a.merge(b, ...) with ticket as the key and a left merge.'
---

# Exercise: Match payments

The payment register contains T4 but has no record for T5. Keep both reservations so the desk can follow up on T5. A missing payment record means the status is unknown; it is not the same as a recorded `False` value.

Match the `ticket` column with a left merge. In the printed result, T4 has its recorded `True` status and T5 has a missing `paid` cell. The payment keys supplied here are unique.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Complete `match_payments(a, b)` with a left merge on `ticket`.
