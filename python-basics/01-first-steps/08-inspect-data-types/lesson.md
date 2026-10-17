---
title: "Inspect Lantern Types"
slug: inspect-data-types
order: 8
language: python
lesson_type: coding
summary: "Inspect string, integer, and float values in Adam’s kit."
seo_title: "Inspect Lantern Types | Python Basics"
seo_description: "Inspect string, integer, and float values in Adam’s kit."
seo_keywords: [python basics, first steps, lantern atlas]
---

You can use `type(value)` to ask Python what kind of data you have in a variable. Run this example and compare the integer, float, and string results.

```python run
age = 25
height = 5.5
name = "Charles"
print(type(age))
print(type(height))
print(type(name))
```

The output includes labels such as `<class 'int'>`. If you want just the short name, add `.__name__` after `type(value)`. Make sure to include those two underscores (`_`) around `name`. These are called attributes, but you will learn more about those in future lesson.

```python run
age = 25
height = 5.5
name = "Charles"
print(type(age).__name__)
print(type(height).__name__)
print(type(name).__name__)
```

This time the lines read as `int`, `float`, and `str`.

In **main.py**, a lantern has a name, a charge count, and a weight. There is also a print statemen right below them to print their values. Change the two numeric assignments, leaving those calls in place.

## Your Tasks

1. Set `charges` to the integer `5`.
2. Set `weight` to the float `3.5`.
