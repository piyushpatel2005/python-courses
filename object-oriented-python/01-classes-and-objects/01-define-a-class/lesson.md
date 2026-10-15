---
title: Define a class
slug: define-a-class
order: 1
language: python
lesson_type: coding
summary: Define an empty class named `Tool` using a `class` statement and `pass`.
seo_title: Define a class | Python OOP practice
seo_description: Define an empty class named `Tool` using a `class` statement and `pass`.
seo_keywords:
- Python OOP
- define a class
- coding practice
---

# Define a class

A community workshop lends tools. Before a program can track individual tools, it needs a name for that kind of thing. You will define that name as a Python class. This first edit is deliberately small: the class has no data or behavior yet.

## A new kind of object

You already use objects such as strings and lists. A class describes a kind of object you can create. The `class` statement defines your own kind, using an indented body just as a function definition does. Class names conventionally start with a capital letter.

```python
class Parcel:
    pass
```

The colon starts the body. `pass` is a statement that does nothing; Python needs it when the body would otherwise be empty. `Parcel` now refers to the class itself. It does not refer to one particular parcel.

Calling the class with parentheses creates an **instance**, an individual object of that class:

```python
first = Parcel()
print(isinstance(first, Parcel))  # True
```

`isinstance(value, ClassName)` checks whether a value is an instance of the named class. You do not need to memorize Python's printed representation of an empty object. It often contains an address-like number that changes between runs.

For now, keep the distinction precise: the class is `Parcel`; `first` refers to one instance. The next lesson will create two objects from one class and show why two variable names are not always two objects.

## The supplied console check

The code below your editing area is a supplied probe. Its `if __name__ == "__main__":` guard runs the probe when you run the file directly, but not when tests import it. The `try`/`except` reports unfinished work without crashing the starter. You only need to edit the marked area, not this check.

## Your Tasks

1. Define an empty class named `Tool` using a `class` statement and `pass`.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. Run should eventually print `Tool instance: True`.
