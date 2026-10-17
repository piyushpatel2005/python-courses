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

You have used strings for names and integers for counts. Other values need different types. For example, a temperature may include a decimal part, while a yes or no answer needs only two possible values.

These four types will appear throughout the next few lessons. Here is a short summary of what they represent and how you can use them in your Python code.

| Python type | What it represents | Example |
| --- | --- | --- |
| `int` | A whole number | `25` |
| `float` | A floating-point number; often written with a decimal point | `75.50` |
| `str` | Text data | `"Adam"` |
| `bool` | A true or false value | `True` |

Let's take a look at example for each of these.

## `int` data

An age or a score is often a whole number. 

```python run
age = 25
print(age)
```

## `float` data

A temperature can have a fractional part. These types of values are stored as a floating-point number with decimal part.

```python run
temperature = 75.50
print(temperature)
```

## `str` data

Names, addresses or even general information are of type string. Even the digits inside this address are part of its text. String data is often referred to as `str` data type in Python.

```python run
name = "Adam"
address = "123 Nucleus Sky Station"
print(name)
print(address)
```

## `bool` data

A boolean records whether something is true or false. Python spells its two values `True` and `False`, with capital first letters and no quotes around it. Those words are reserved keywrods so you cannot use them as variable names. A boolean data type is called `bool` in Python.

Variable names for boolean data types are usually defined with meaningful name; often beginning with `is_` or `has_` to make them easy to read in your code.

```python run
is_adult = True
has_license = False
print(is_adult)
print(has_license)
```

Next, let's learn about how you can actually check the data type for a variable.
