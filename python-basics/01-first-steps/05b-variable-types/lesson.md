---
title: "Variable Types"
slug: variable-types
order: 1
language: python
lesson_type: interactive
summary: "Learn about different data types of variables in Python."
seo_title: "Variable Types | Python Basics"
seo_description: "Learn about Python variable data types"
seo_keywords: [python basics, variable data types]
---

So far, you've used string and integer variables to store information, but let's say you want to convey information about temperature in your space shuttle. You would need it to be precise because it will be very important to maintain it for the crew members. This is where other types of variables can come in. Let's see what variable types we have in Python.

Python offers several built-in data types. Some of the most common ones are:

1. Integer: Whole numbers
2. Float: Decimal numbers
3. String: Textual information
4. Boolean: True or False values

Integers are whole numbers without any decimal points. Information like age, scores, points, etc. are usually in the form of whole numbers and they are stored using integer data types.

```python run
age = 25
print(age)
```

On the other hands, information like temperature, price, height etc. can be store in the form of decimal numbers. For example, the temperature outside is 75.5 degrees. This is where float data types can be used.

```python run
temperature = 75.5
print(temperature)
```

Textual information like name, address, etc. can be stored using string data type in Python. You have already seen this in previous examples.

```python run
name = "Adi"
address = "123 Nucleus Sky Station"
print(name)
print(address)
```

Boolean data types can be used for decision making in your code. They can have values like `True` or `False`. These are reserved keywords in Python, and you cannot create a variable with this names. It's convention to name your boolean variables starting with `is` or `has` to indicate the type of data they store.

```python run
is_adult = True
has_license = False
print(is_adult)
print(has_license)
```

