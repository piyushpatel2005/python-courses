---
title: Initialize an object
slug: initialize-an-object
order: 9
language: python
lesson_type: coding
summary: Implement `GameItem.__init__(self, name, uses)` to store both arguments as instance attributes named `name` and `uses`.
seo_title: Initialize an object | Python OOP practice
seo_description: Implement `GameItem.__init__(self, name, uses)` to store both arguments as instance attributes named `name` and
  `uses`.
seo_keywords:
- Python OOP
- initialize an object
- coding practice
---

# Initialize an object

Creating an item should also give it the data its methods need. Move setup into the class so `GameItem("lantern", 4)` produces an item with a name and an activation count in one call.

## Python calls the initializer

A method named `__init__` runs automatically when a normal class call creates an instance. The name has two underscores on each side. This is one of Python's special method names; spelling it `init` will not have the same effect.

```python
class Waypoint:
    def __init__(self, region):
        self.region = region

waypoint = Waypoint("North Grove")
print(waypoint.region)
```

Python creates the instance and passes it as `self`. The argument supplied by the caller becomes `region`. The assignment stores that argument on the new object, where it remains accessible after the initializer finishes.

The parameter and attribute can have the same name because they live in different places. `region` reads the local parameter; `self.region` accesses the object's attribute. Writing only `region = region` would leave the object without the needed attribute.

Do not return the newly created object from `__init__`. The class call handles returning the instance; `__init__` initializes it and must return `None`, usually by having no return statement. People often call the class call a constructor. More precisely, this method handles initialization, not allocation.

The supplied `summary` method expects `name` and `uses` to exist. Your initializer creates those attributes from its arguments. You do not need the old `make_item` helper anymore, and callers should not have to attach data manually.

The probe constructs two items with different inputs. Both use the same initializer code, but each call gets its own `self`. Changing one item later must not overwrite the other item's state.

## Your Tasks

1. Implement `GameItem.__init__(self, name, uses)` to store both arguments as instance attributes named `name` and `uses`.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints a separate summary for each constructed item.
