---
title: Compare Workshop Supplies
slug: comparisons-and-booleans
order: 1
language: python
lesson_type: interactive
summary: Compare quantities and combine true-or-false checks for a workshop supply plan.
seo_title: Python Comparisons and Booleans | Python Basics
seo_description: Run small Python examples to learn comparison operators, True and False, and the and, or, and not operators.
seo_keywords: [python comparisons, python booleans, logical operators]
---

# Compare workshop supplies

Before opening the community workshop, you can check whether the art table has enough paint. A comparison returns `True` or `False` (capitalized in Python). `=` stores a value; `==` compares two values. Run this check, then try changing `paint_tubes` to `4`.

```python run
paint_tubes = 6
print(paint_tubes >= 5)
print(paint_tubes == 5)
```

`>` and `<` mean greater and less; `>=` and `<=` include equality. `!=` means not equal. You can combine checks: `and` needs both to be true, `or` needs at least one, and `not` reverses a boolean. Parentheses make a combined check easy to read.

```python run
markers = 8
paper_packs = 2
print(markers >= 6 and paper_packs >= 2)
print(markers < 6 or paper_packs < 2)
print(not (markers == 0))
```

These results can guide the decisions in the next lesson. Try changing `paper_packs` to `1` and run the second block again.
