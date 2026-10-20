---
title: "Exercise: Update a Shop Notice"
slug: exercise-clean-notice
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: Clean a shop notice, replace its status and check its prefix.
seo_title: "Exercise: Update a Shop Notice | Python Basics"
seo_description: Clean a shop notice, replace its status and check its prefix.
seo_keywords: [python basics, strings, python strings, replace, startswith]
---

# Exercise: update a shop notice

The printed notice has inconsistent spaces and capitalization: `"  SHOP CLOSED  "`. Make a clean copy, prepare the open version, and check which business the notice belongs to.

Keep `raw_notice` unchanged. Store each result separately so you can compare them.

## Your Tasks

1. Set `notice` to `raw_notice` with surrounding whitespace removed and letters lowercased.
2. Set `updated_notice` to a copy of `notice` with `closed` replaced by `open`.
3. Set `is_shop_notice` to whether `notice` starts with `shop`.

Use the methods from the previous lesson. Run after each task; unfinished results show `None`. The finished line reads `shop closed shop open True`. Submit to check all three results.
