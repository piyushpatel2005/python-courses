---
title: Attach instance data
slug: attach-instance-data
order: 3
language: python
lesson_type: coding
summary: Inside `make_item(name)`, attach the supplied `name` value to the new item as its `name` instance attribute.
seo_title: Attach instance data | Python OOP practice
seo_description: Inside `make_item(name)`, attach the supplied `name` value to the new item as its `name` instance attribute.
seo_keywords:
- Python OOP
- attach instance data
- coding practice
---

# Attach instance data

The inventory needs a name for each item. Give every new object the name passed to `make_item`, whether it is a lantern, a shield, or something else. The helper supplies the object creation and return so you can focus on one attribute assignment.

## Attributes belong to objects

An **attribute** is a named value accessed through an object. Use a dot between the object's name and the attribute's name. With these ordinary classes, assignment can create an attribute after the instance exists.

```python
class Checkpoint:
    pass

beacon = Checkpoint()
beacon.region = "clearing"
print(beacon.region)  # clearing
```

`region` is not a separate global variable here. It is attached to the particular object referred to by `beacon`. Another `Checkpoint()` starts without that attribute. Reading an attribute that does not exist raises `AttributeError`; spelling matters on both sides of the dot.

A function parameter can supply an attribute's value just as it can supply any assignment's value. For example, a function accepting `region` could store that parameter on a checkpoint. Avoid quoting a parameter name: `"region"` is literal text, while `region` reads the value passed to the function.

The editor already creates a `GameItem` inside `make_item(name)` and returns it. Add one assignment between those lines. You are not writing a method yet: this is an ordinary function that accepts text, builds an object, and returns the object to its caller.

The probe calls the function twice with different names. Treat these as examples, not the only supported inputs. The function should preserve whichever name its caller supplies, and each call should still return a fresh item. In a few lessons, you will move this setup into the class itself so callers cannot forget it.

## Your Tasks

Now it’s your turn to write some code.

1. Inside `make_item(name)`, attach the supplied `name` value to the new item as its `name` instance attribute.

Click **Run** to inspect the results in the console, then click **Submit** when you’re done. The completed probe prints `GameItem names: lantern shield`.
