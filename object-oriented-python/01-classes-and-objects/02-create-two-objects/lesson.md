---
title: Create two objects
slug: create-two-objects
order: 2
language: python
lesson_type: coding
summary: Set `drill` and `saw` to two distinct instances of the supplied `Tool` class.
seo_title: Create two objects | Python OOP practice
seo_description: Set `drill` and `saw` to two distinct instances of the supplied `Tool` class.
seo_keywords:
- Python OOP
- create two objects
- coding practice
---

# Create two objects

The workshop owns two tools of the same kind. Defining a class once is enough, but you must call it twice to represent two separate items. The `Tool` class is supplied; your edit creates the objects.

## Calls create; assignments name

```python
class Ticket:
    pass

morning = Ticket()
evening = Ticket()
print(morning is evening)  # False
```

Each call to `Ticket()` creates a new instance. The `is` operator asks whether two expressions refer to the very same object. It does not compare descriptions, labels, or other data. Here there are two calls, so there are two objects.

An assignment by itself does not create another instance:

```python
spare_name = morning
print(spare_name is morning)  # True
```

Both names now refer to the morning ticket. This is called an alias. If you later attach data through one name, the other name will see it because there is only one object involved. By contrast, the evening ticket remains a separate object.

You might be used to reading `=` as mathematical equality. In Python assignment binds a name to an object. The expression on the right runs first, then the name on the left refers to its result. That is why `Ticket()` and `morning` behave differently on the right side of an assignment.

Use `is` for this identity question. Later lessons will explain how objects can compare their values; two separate objects may represent equal values without being the same object.

In the editor, leave the supplied empty class alone. Replace the two placeholders with class calls. The probe checks the types as well as whether the names refer to distinct objects, so a pair of unrelated values is not enough.

## Your Tasks

1. Set `drill` and `saw` to two distinct instances of the supplied `Tool` class.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `True` for both checks.
