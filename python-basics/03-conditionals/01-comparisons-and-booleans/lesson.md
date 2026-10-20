---
title: "Compare Workshop Supplies"
slug: comparisons-and-booleans
order: 1
language: python
lesson_type: coding
summary: "Compare paint-tube counts and read True or False results."
seo_title: "Python Comparison Operators | Python Basics"
seo_description: "Use ==, !=, <, >, <=, and >= to compare values and produce booleans."
seo_keywords: [python comparisons, comparison operators, python booleans]
---

A community art workshop needs at least five tubes of paint. A comparison lets its organizer check the supply count. The result is a boolean: `True` or `False`. A single `=` is used to assign a value whereas `==` is used to verify if two values are equal.

## Comparison Operators

What good is a programming language if it cannot compare two numbers? So, that's why Python provides comparison operators.

| Operator | Meaning | Example |
| --- | --- | --- |
| `==` | equal to | `4 == 4` is `True` |
| `!=` | not equal to | `4 != 5` is `True` |
| `>` | greater than | `5 > 4` is `True` |
| `<` | less than | `4 < 5` is `True` |
| `>=` | greater than or equal to | `4 >= 4` is `True` |
| `<=` | less than or equal to | `4 <= 4` is `True` |

Try these comparisons with **Run**:

```python run
print(4 < 2)
print(4 >= 4)
print("hi" == "Hello")
print("Hi" != "hi")
```

They print `False`, `True`, `False`, `True`. Text is case-sensitive, so `"Hi"` differs from `"hi"`. In the code editor, six paint tubes make `paint_tubes >= 5` true and `paint_tubes == 5` false.

## Your Tasks

1. Change `paint_tubes` to `4` without removing either comparison. Both lines should now print `False`.

Edit `main.py`, press **Run** to see the results, then **Submit**. You'll write your own comparisons next.
