---
title: "Demo: Inspect Lantern Types"
slug: inspect-data-types
order: 8
language: python
lesson_type: coding
summary: "Inspect string, integer, and float values in Adi’s kit."
seo_title: "Demo: Inspect Lantern Types | Python Basics"
seo_description: "Inspect string, integer, and float values in Adi’s kit."
seo_keywords: [python basics, first steps, lantern atlas]
---

Use `type(value)` to ask Python what kind of value you have. Run this example and compare the integer, float, and string results:

```python run
age = 25
height = 5.5
name = "Charles"
print(type(age))
print(type(height))
print(type(name))
```

The output includes labels such as `<class 'int'>`. If you want just the short name, add `.__name__` after `type(value)`. You can use that spelling here without learning the details of attributes yet.

```python run
age = 25
height = 5.5
name = "Charles"
print(type(age).__name__)
print(type(height).__name__)
print(type(name).__name__)
```

This time the lines read `int`, `float`, and `str`.

In **main.py**, a lantern has a name, a charge count, and a weight. The supplied print calls show each value beside its type. Change the two numeric assignments, leaving those calls in place.

Press **Run** to check for `5 int` and `3.5 float`, then **Submit**. The values change, but their types stay the same.

## Your Tasks

1. Set `charges` to the integer `5`.
2. Set `weight` to the float `3.5`.
