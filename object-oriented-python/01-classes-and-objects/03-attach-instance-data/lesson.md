---
title: Attach instance data
slug: attach-instance-data
order: 3
language: python
lesson_type: coding
summary: Inside `make_tool(name)`, attach the supplied `name` value to the new tool as its `name` instance attribute.
seo_title: Attach instance data | Python OOP practice
seo_description: Inside `make_tool(name)`, attach the supplied `name` value to the new tool as its `name` instance attribute.
seo_keywords:
- Python OOP
- attach instance data
- coding practice
---

# Attach instance data

An empty tool object cannot tell you which tool it represents. Add a name to each new object so the workshop can distinguish a drill from a saw. The supplied `make_tool` function gives you a small place to practice without repeating the setup code.

## Attributes belong to objects

An **attribute** is a named value accessed through an object. Use a dot between the object's name and the attribute's name. With these ordinary classes, assignment can create an attribute after the instance exists.

```python
class Plant:
    pass

fern = Plant()
fern.location = "window"
print(fern.location)  # window
```

`location` is not a separate global variable here. It is attached to the particular object referred to by `fern`. Another `Plant()` starts without that attribute. Reading an attribute that does not exist raises `AttributeError`; spelling matters on both sides of the dot.

A function parameter can supply an attribute's value just as it can supply any assignment's value. For example, a function accepting `location` could store that parameter on a plant. Avoid quoting a parameter name: `"location"` is literal text, while `location` reads the value passed to the function.

The editor already creates a `Tool` inside `make_tool(name)` and returns it. Add one assignment between those lines. You are not writing a method yet: this is an ordinary function that accepts text, builds an object, and returns the object to its caller.

The probe calls the function twice with different names. Treat these as examples, not the only supported inputs. The function should preserve whichever name its caller supplies, and each call should still return a fresh tool. In a few lessons, you will move this setup into the class itself so callers cannot forget it.

## Your Tasks

1. Inside `make_tool(name)`, attach the supplied `name` value to the new tool as its `name` instance attribute.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `Tool names: drill saw`.
