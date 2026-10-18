---
title: "Compare Workshop Supplies"
slug: comparisons-and-booleans
order: 1
language: python
lesson_type: coding
summary: "Use comparison operators to check workshop supplies and read boolean results."
seo_title: "Python Comparison Operators | Python Basics"
seo_description: "Compare numbers and text with ==, !=, <, >, <=, and >= to get True or False."
seo_keywords: [python comparisons, comparison operators, python booleans]
---

At the Golden Gate, a decision starts with a question: are there enough supplies? A comparison gives a boolean result, either `True` or `False`. You have used `=` to assign a value to a name. To ask whether two values are equal, use `==` instead.

## Comparison operators

| Operator | Meaning | Example |
| --- | --- | --- |
| `==` | equal to | `4 == 4` is `True` |
| `!=` | not equal to | `4 != 5` is `True` |
| `>` | greater than | `5 > 4` is `True` |
| `<` | less than | `4 < 5` is `True` |
| `>=` | greater than or equal to | `4 >= 4` is `True` |
| `<=` | less than or equal to | `4 <= 4` is `True` |

Press **Run** to compare numbers and text:

```python run
print(4 < 2)
print(4 >= 4)
print("hi" == "Hello")
print("Hi" != "hi")
```

The results are `False`, `True`, `False`, and `True`. Text comparisons are case-sensitive: `"Hi"` and `"hi"` differ. The editable `main.py` asks two questions about paint tubes: is the supply at least five, and is it exactly five? With six tubes, the answers are `True` and `False`.

## Your Tasks

1. Change `paint_tubes` to `4` while keeping both comparisons. The two answers should now be `False` and `False`.

Edit `main.py`, press **Run** to see both answers, then **Submit**. The next exercise lets you write comparisons yourself. Logical operators, which combine boolean results, have their own lesson after that.
