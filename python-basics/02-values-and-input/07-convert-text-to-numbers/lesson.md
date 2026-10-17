---
title: "Convert Shard Text"
slug: convert-text-to-numbers
order: 7
language: python
lesson_type: coding
summary: "Convert a text count before adding bonus shards."
seo_title: "Convert Shard Text | Python Basics"
seo_description: "Convert a text count before adding bonus shards."
seo_keywords: [python basics, values and input, lantern atlas, type cast in python]
---

A count can look like a number but still can be text. The quotes around a number makes the difference: `"12" + "3"` joins strings to make `"123"` text. To add a numeric amount, first convert the text with `int()`, as in `int("12") + 3`. If you try to add text to a number, you get an error without this conversion.

```python run
print("12" + 3)
```

```python run
print(int("12") + 3)
```
There are a few related conversions to recognize:

- `float("2.5")` converts decimal text to a float.
- `str(15)` converts a number to text.
- `int(3.9)` gives `3`: it discards the fractional part rather than rounding to the nearest integer.

The text must match the conversion. For example, `int("many")` raises a `ValueError` because Python cannot read it as an integer. You will learn to handle errors later.

```python run
print(float("2.5"))
print(str(15))
print(int(3.9))
```

You could also check the types after the conversion using the `type()` function.

```python run
print(type(int("12")))
print(type(float("2.5")))
print(type(str(15)))
```

The code in the editor reads a shard count from a string, converts it to an integer, and adds a bonus. Keep that conversion in place when you change the text.

## Your Tasks

1. Set `shard_text` to `"15"`.

Press **Run** to see `Shards: 17`, then **Submit**.