---
title: "Demo: Inspect Lantern Types"
slug: inspect-data-types
order: 6
language: python
lesson_type: coding
summary: "Inspect string, integer, and float values in Adi’s kit."
seo_title: "Demo: Inspect Lantern Types | Python Basics"
seo_description: "Inspect string, integer, and float values in Adi’s kit."
seo_keywords: [python basics, first steps, lantern atlas]
---

You can check the data type of a variable using `type()` function in Python.

```python run
age = 25
height = 5.5
name = "Charles"
print(type(age))
print(type(height))
print(type(name))
```

If you only want to see the data type, you could use `type().__name__`.

```python run
age = 25
height = 5.5
name = "Charles"
print(type(age).__name__)
print(type(height).__name__)
print(type(name).__name__)
```

Here, a lantern name is `str`, The `charges` variable contains value of type `int`, and the `weight` variable contains value of type `float`. Python infers these types from values; `type(value).__name__` shows the short name. In **main.py**, change only `weight` from `2.5` to `3.5`. Press **Run** to see the weight change while its type stays `float`, then **Submit**. Booleans and collections come later.

## Your Tasks

1. In this code snippet, assign `charges` with an integer value `5`.
2. Set `weight` with a float value `3.5`.

