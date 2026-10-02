---
title: "Exercise: Decode a Rune Notice"
slug: exercise-clean-notice
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: Clean a rune notice, replace its state, and check its prefix.
seo_title: "Exercise: Decode a Rune Notice | Python Basics"
seo_description: Clean a rune notice, replace its state, and check its prefix.
seo_keywords: [python basics, strings, lantern atlas]
---

# Exercise: Decode a Rune Notice

Ari needs a readable route status from the cavern wall. First normalize the rune text, then produce a restored-state message and check whether it belongs to a beacon. Keep `raw_notice` unchanged. Edit `main.py`, Run, then Submit.

## Your Tasks

1. Set `notice` to the stripped, lowercased `raw_notice`.
2. Set `lit_notice` to `notice` with `dim` replaced by `lit`.
3. Set `is_beacon_notice` to whether `notice` starts with `beacon`.
