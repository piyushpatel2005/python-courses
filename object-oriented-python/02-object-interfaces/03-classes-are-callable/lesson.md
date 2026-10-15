---
title: Classes are callable
slug: classes-are-callable
order: 3
language: python
lesson_type: coding
summary: Implement `create_record(factory, name)` to call the supplied factory exactly once with `name` and return the object
  it produces.
seo_title: Classes are callable | Python OOP practice
seo_description: Implement `create_record(factory, name)` to call the supplied factory exactly once with `name` and return
  the object it produces.
seo_keywords:
- Python OOP
- classes are callable
- coding practice
---

# Classes are callable

A registration helper should create an object without deciding which class the caller wants. Pass the class as an argument, then call that argument. A class name is a reference to a callable object, not special syntax that only works in one fixed place.

## Pass the class, not an instance

```python
class Greeting:
    def __init__(self, name):
        self.text = f"Hello, {name}"

def build(factory, value):
    return factory(value)

message = build(Greeting, "Nia")
print(message.text)  # Hello, Nia
```

Inside `build`, the parameter `factory` refers to the class `Greeting`. The call `factory(value)` therefore constructs a greeting. The outer call passes `Greeting` without parentheses; construction happens inside the helper where the needed argument is available.

If the caller passed `Greeting("Nia")` instead, it would construct an instance too early and pass that instance to the helper. Our ordinary instances are not callable. Classes and their instances are different objects, even when both appear in the same expression.

This helper is sometimes called a factory because it produces objects. A factory does not have to be a class: an ordinary function can also accept an argument and return an object. For this exercise, support any callable accepting one name, without checking its exact type.

The editor supplies `Tool` and `Member`, each with a one-argument initializer. Your `create_record(factory, name)` function should call the given factory exactly once with the given name and return its result. It should not always construct `Tool`, and it should not discard a result and construct another object.

The probe uses both supplied classes. Seeing the two names is only the visible check; Submit also tries a function factory so that the implementation depends on the supplied callable rather than a fixed class name.

## Your Tasks

1. Implement `create_record(factory, name)` to call the supplied factory exactly once with `name` and return the object it produces.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints a tool name and a member name from the same helper.
