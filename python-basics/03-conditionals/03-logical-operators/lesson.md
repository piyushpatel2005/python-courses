---
title: "Combine Checks with Logical Operators"
slug: logical-operators
order: 3
language: python
lesson_type: coding
summary: "Combine boolean checks with and, or, and not."
seo_title: "Python Logical Operators | Python Basics"
seo_description: "Learn when and, or, and not make combined checks true or false."
seo_keywords: [python logical operators, and or not, boolean checks]
---

A single comparison answers one question. A gate may need to ask more than one: are the markers ready **and** is there enough paper? Python's logical operators combine or reverse boolean checks.

## `and`, `or`, and `not`

| Operator | Result |
| --- | --- |
| `and` | `True` only when both checks are true |
| `or` | `True` when at least one check is true |
| `not` | Reverses `True` and `False` |

Try this separate example. The first check passes because both supplies meet their minimum; the second passes because at least one supply is low.

```python run
ropes = 3
hooks = 0
print(ropes >= 2 and hooks >= 1)
print(ropes < 2 or hooks < 1)
print(not (hooks == 0))
```

It prints `False`, `True`, `False`. The parentheses around `hooks == 0` show which result `not` reverses. `not` applies to a boolean expression; it does not change `hooks` itself.

In the editable `main.py`, the workshop starts with eight markers and two paper packs. Its three combined checks print `True`, `False`, `True`. Changing one supply at a time lets you see which answers change.

## Your Tasks

1. Set `paper_packs` to `1`. The `and` and `or` lines should print `False` and `True`.
2. Set `markers` to `0`. The final `not` line should print `False`.

Edit `main.py`, press **Run** after each change, then **Submit**. The next exercise asks you to write these operators yourself.
