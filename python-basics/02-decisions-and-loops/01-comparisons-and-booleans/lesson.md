---
title: Compare Gate Signals
slug: comparisons-and-booleans
order: 1
language: python
lesson_type: interactive
summary: Compare beacon charge and combine boolean checks before Ari approaches a gate.
seo_title: Python Comparisons and Booleans | Python Basics
seo_description: Compare charge levels and logical conditions in The Lantern Atlas.
seo_keywords: [python comparisons, python booleans, logical operators]
---

# Compare gate signals

Ari reaches a gate that opens only when the nearby beacon has enough charge. A comparison returns `True` or `False` (capitalized in Python). `=` stores a value; `==` compares two values. Run this check to see how one value can pass a threshold but fail an equality test.

```python run
charge = 6
print(charge >= 5)
print(charge == 5)
```

`>` and `<` mean greater and less; `>=` and `<=` include equality. `!=` means not equal. Combine checks with `and` (both), `or` (either), and `not` (reverse). Parentheses clarify a combined check.

```python run
glowstones = 8
spare_cells = 2
print(glowstones >= 6 and spare_cells >= 2)
print(glowstones < 6 or spare_cells < 2)
print(not (glowstones == 0))
```

The next trial uses those true-or-false results to choose a gate signal.
