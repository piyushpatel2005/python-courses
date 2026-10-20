---
title: "Combine Checks with Logical Operators"
slug: logical-operators
order: 3
language: python
lesson_type: coding
summary: "Combine stock checks with and, or, and not."
seo_title: "Python Logical Operators | Python Basics"
seo_description: "See how and, or, and not combine or reverse boolean results."
seo_keywords: [python logical operators, and or not, boolean checks]
---

A workshop may need both markers and paper before it can start. Python combines comparisons with logical operators.

## Logical Operators

| Operator | Result |
| --- | --- |
| `and` | `True` only if both checks are true |
| `or` | `True` if at least one check is true |
| `not` | Reverses a boolean result |

The example below checks whether a repair kit has enough rope and hooks:

```python run
ropes = 3
hooks = 0
print(ropes >= 2 and hooks >= 1)
print(ropes < 2 or hooks < 1)
print(not (hooks == 0))
```

It prints `False`, `True`, `False`. There aren't enough hooks. Notice you put parentheses around the third line check. Python evaluates the expression inside the parentheses first and then applies the `not` operator to the result. It's always a good idea to put parentheses to make it clear.

The code in the editor starts with eight markers and two packs of paper. Its three lines print `True`, `False`, `True`. Change one supply at a time to see which results depend on it.

## Your Tasks

1. Set `paper_packs` to `1`. The `and` and `or` results become `False` and `True`.
2. Set `markers` to `0`. The final `not` result becomes `False`.

Edit `main.py`, press **Run** after each change, then **Submit**. Next you'll write the expressions instead of changing their inputs.
