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

Clean the notice from the cavern wall, then prepare a message for the restored beacon. You'll also check whether the text starts with the word `beacon`.

Keep `raw_notice` as it is. Each result belongs in its own variable, so you can inspect what changed.

## Your Tasks

1. Set `notice` to `raw_notice` with surrounding whitespace removed and letters lowercased.
2. Set `lit_notice` to a copy of `notice` with `dim` replaced by `lit`.
3. Set `is_beacon_notice` to the result of checking whether `notice` starts with `beacon`.

Use the string methods from the previous lesson. Run `main.py` after each task; unfinished values will still show `None`. The completed output should be `beacon dim beacon lit True`. Submit to check the three results.
