---
title: "Echo Tower: Sum the Signals"
slug: exercise-recursive-ticket-sum
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Combine short beacon signals with a recursive sum.
seo_title: "Echo Tower: Sum the Signals | Python Basics"
seo_description: Combine short beacon signals with a recursive sum.
seo_keywords: [python recursive sum, beacon signals, base case]
---

This time the tower receives a list of signal strengths, and you need one total. The recursive idea is to add the first strength to the total of the remaining list. An empty list returns zero and ends the calls.

For example, `[4, 2]` reduces to `4 + 2 + 0`. Use indexing for the first value and a slice for the remaining values.

Complete the helper in `main.py`. Run should show `Beacon signal: 6`, then Submit. Use short lists while you practise tracing the calls.

## Your Task

1. Complete `signal_total(signals)`: return `0` for an empty list; otherwise return the first signal plus a recursive call on the remaining slice, `signals[1:]`.
