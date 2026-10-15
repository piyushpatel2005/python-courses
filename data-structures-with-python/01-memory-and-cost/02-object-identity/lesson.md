---
title: "Object identity without addresses"
slug: object-identity
order: 2
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `identity_flags(items, target)` to return a fresh ordered list of identity comparisons."
seo_title: "Object identity without addresses | Python data structures"
seo_description: "Practice object identity through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - object identity
  - data structures practice
---

# Object identity without addresses

Two containers can hold equal contents without being the same container. A cache of open trays must distinguish a second reference to an existing tray from a newly created tray with identical contents. Equality alone cannot answer that question.

## Two different questions

Use `==` to ask whether values compare equal. Use `is` to ask whether references designate the same object. Lists compare their elements for equality, so two separately created empty lists are equal. They are not identical. An alias compares both equal and identical to its original.

```python
left = ["cedar"]
right = ["cedar"]
shared = left
print(left == right, left is right)  # True False
print(left is shared)               # True
```

`id(object)` returns an identity token that remains stable during that object's lifetime. Do not interpret the number as a portable memory address or expect any particular distance between two tokens. Python implementations may represent objects differently, and a token may be reused after an object is gone. Direct `is` comparisons express the question more clearly here.

## Find the alias, not the equal value

Write `identity_flags(items, target)` to visit the references in `items` and produce one Boolean per position. A position is true only when its object is `target`. Preserve order and repeated references. Do not change either the input container or its elements. The output is a new list so callers may edit the flags without editing their input.

For a list of n references, this operation performs n identity comparisons and creates n flags: O(n) time and O(n) output space. Identity comparison itself does not scan a list's contents. Equality might scan contents and can also be customized by a class, which is another reason not to substitute it. Avoid exercises based on whether small integers or strings happen to share objects; this lesson uses explicitly created mutable objects whose sharing is deliberate.

## Build in small steps

This is one small transformation. Either a comprehension or a loop building the Boolean list is suitable; no separate validation step is required.

## Your Tasks

1. Return one identity comparison per item, preserving order.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
