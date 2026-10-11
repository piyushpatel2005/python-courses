---
title: "Variable Types"
slug: variable-types
order: 7
language: python
lesson_type: interactive
summary: "Learn about different data types of variables in Python."
seo_title: "Variable Types | Python Basics"
seo_description: "Learn about Python variable data types"
seo_keywords: [python basics, variable data types]
---

You have used strings for names and integers for counts. Other values need different types: a temperature may include a decimal part, while a yes-or-no answer needs only two possible values.

These four types will appear throughout the next few lessons:

| Python type | What it represents | Example |
| --- | --- | --- |
| `int` | A whole number | `25` |
| `float` | A floating-point number, often written with a decimal point | `75.5` |
| `str` | Text | `"Adi"` |
| `bool` | A true-or-false value | `True` |

An age or a score is often a whole number. Run this integer example:

```python run
age = 25
print(age)
```

A temperature can have a fractional part. This value is a float:

```python run
temperature = 75.5
print(temperature)
```

Names and addresses are strings. Even the digits inside this address are part of its text:

```python run
name = "Adi"
address = "123 Nucleus Sky Station"
print(name)
print(address)
```

A boolean records whether something is true or false. Python spells its two values `True` and `False`, with capital first letters and no quotes. Those words are reserved; you cannot use them as variable names.

Names beginning with `is_` or `has_` often make boolean values easy to read:

```python run
is_adult = True
has_license = False
print(is_adult)
print(has_license)
```

Run each example and compare its output with its value in the code. The next lesson shows how to ask Python for a value's type instead of deciding from its appearance.
