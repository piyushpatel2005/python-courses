---
title: Define a class
slug: define-a-class
order: 1
language: python
lesson_type: coding
summary: Define an empty class named `GameItem` using a `class` statement and `pass`.
seo_title: Define a class | Python OOP practice
seo_description: Define an empty class named `GameItem` using a `class` statement and `pass`.
seo_keywords:
- Python OOP
- define a class
- coding practice
---

# Define a class

Mosslight Studio is building Lantern Vale, a small exploration game. You will start with the Python objects behind its inventory, not graphics or controls. Define a class for game items first; later lessons will give each item data and behavior.

## A new kind of object

You already use objects such as strings and lists. A class describes a kind of object you can create. The `class` statement defines your own kind, using an indented body just as a function definition does. Class names conventionally start with a capital letter.

```python
class Portal:
    pass
```

The colon starts the body. `pass` is a statement that does nothing; Python needs it when the body would otherwise be empty. `Portal` now refers to the class itself. It does not refer to one particular portal.

Calling the class with parentheses creates an **instance**, an individual object of that class:

```python
first = Portal()
print(isinstance(first, Portal))  # True
```

`isinstance(value, ClassName)` checks whether a value is an instance of the named class. You do not need to memorize Python's printed representation of an empty object. It often contains an address-like number that changes between runs.

For now, keep the distinction precise: the class is `Portal`; `first` refers to one instance. The next lesson will create two objects from one class and show why two variable names are not always two objects.

## The supplied console check

The code below your editing area is a supplied probe. Its `if __name__ == "__main__":` guard runs the probe when you run the file directly, but not when tests import it. The `try`/`except` reports unfinished work without crashing the starter. You only need to edit the marked area, not this check.

## Your Tasks

Now it’s your turn to write some code.

1. Define an empty class named `GameItem` using a `class` statement and `pass`.

Click **Run** to inspect the results in the console, then click **Submit** when you’re done. Run should eventually print `GameItem instance: True`.
