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

A count can look like a number but still be text. Quotes make the difference: `"12" + "3"` joins strings to make `"123"`. To add a numeric amount, first convert the text with `int()`, as in `int("12") + 3`.

The starter reads a shard count from a string, converts it to an integer, and adds a bonus. Keep that conversion in place when you change the text.

There are a few related conversions to recognize:

- `float("2.5")` converts decimal text to a float.
- `str(15)` converts a number to text.
- `int(3.9)` gives `3`: it discards the fractional part rather than rounding to the nearest integer.

The text must match the conversion. For example, `int("many")` raises a `ValueError` because Python cannot read it as an integer. You will learn to handle errors later.

Edit **main.py**, keeping quotes around `shard_text`. Press **Run** to see `Shards: 17`, then **Submit**.

## Your Tasks

1. Set `shard_text` to `"15"`.
