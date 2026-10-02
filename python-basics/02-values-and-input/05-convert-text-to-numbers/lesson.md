---
title: "Demo: Convert Shard Text"
slug: convert-text-to-numbers
order: 5
language: python
lesson_type: coding
summary: "Convert a text count before adding bonus shards."
seo_title: "Demo: Convert Shard Text | Python Basics"
seo_description: "Convert a text count before adding bonus shards."
seo_keywords: [python basics, values and input, lantern atlas]
---

A response can look numeric but still be text: `"12" + "3"` yields `"123"`, while `int("12") + 3` yields `15`. `float("2.5")` reads decimal text, `str(15)` makes text, and `int(3.9)` truncates instead of rounding. Invalid text raises `ValueError`. Change only `shard_text` from `"12"` to `"15"` in **main.py**. Press **Run** for `Shards: 17`, then **Submit**.

## Your Tasks

1. Set `shard_text` to `"15"` and keep its `int()` conversion.
