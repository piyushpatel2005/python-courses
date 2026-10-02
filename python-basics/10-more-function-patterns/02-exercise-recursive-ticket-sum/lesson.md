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

The tower now receives a short list of signal strengths. Unlike the countdown demo, this function returns **one total**: the first strength plus the total of the shorter list. An empty list contributes zero and ends the calls.

Edit `main.py`, Run to check `Beacon signal: 6`, then Submit. The editor starts with an unfinished function; no keyboard input is needed. Use small lists here because deep recursion has a limit.

## Your Task

1. Complete `signal_total(signals)` recursively: return `0` for an empty list; otherwise return `signals[0] + signal_total(signals[1:])`.
