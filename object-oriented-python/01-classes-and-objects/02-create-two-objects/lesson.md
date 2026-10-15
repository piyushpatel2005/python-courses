---
title: Create two objects
slug: create-two-objects
order: 2
language: python
lesson_type: coding
summary: Set `lantern` and `shield` to two distinct instances of the supplied `GameItem` class.
seo_title: Create two objects | Python OOP practice
seo_description: Set `lantern` and `shield` to two distinct instances of the supplied `GameItem` class.
seo_keywords:
- Python OOP
- create two objects
- coding practice
---

# Create two objects

A lantern and a shield belong to the same category in the inventory, but they need separate objects. The supplied `GameItem` class describes that category. Call it once for each item so changing one will not change the other.

## Calls create; assignments name

```python
class Portal:
    pass

forest = Portal()
cave = Portal()
print(forest is cave)  # False
```

Each call to `Portal()` creates a new instance. The `is` operator asks whether two expressions refer to the very same object. It does not compare descriptions, labels, or other data. Here there are two calls, so there are two objects.

An assignment by itself does not create another instance:

```python
spare_name = forest
print(spare_name is forest)  # True
```

Both names now refer to the forest portal. This is called an alias. If you later attach data through one name, the other name will see it because there is only one object involved. By contrast, the cave portal remains a separate object.

You might be used to reading `=` as mathematical equality. In Python assignment binds a name to an object. The expression on the right runs first, then the name on the left refers to its result. That is why `Portal()` and `forest` behave differently on the right side of an assignment.

Use `is` for this identity question. Later lessons will explain how objects can compare their values; two separate objects may represent equal values without being the same object.

In the editor, leave the supplied empty class alone. Replace the two placeholders with class calls. The probe checks the types as well as whether the names refer to distinct objects, so a pair of unrelated values is not enough.

## Your Tasks

Now it’s your turn to write some code.

1. Set `lantern` and `shield` to two distinct instances of the supplied `GameItem` class.

Click **Run** to inspect the results in the console, then click **Submit** when you’re done. The completed probe prints `True` for both checks.
