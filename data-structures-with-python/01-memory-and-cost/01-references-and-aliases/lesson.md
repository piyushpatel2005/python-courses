---
title: "References and aliases"
slug: references-and-aliases
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `append_shared(items, value)` to append once and return the same list object."
seo_title: "References and aliases | Python data structures"
seo_description: "Practice references and aliases through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - references and aliases
  - data structures practice
---

# References and aliases

A shared packing list should show additions made by either volunteer. The two names do not need two lists: they can refer to one list object. Your first operation will make that sharing visible without relying on a printed memory address.

## Read the type hints

Function headers include small notes about intended types. In `values: list[int]`, `list[int]` means a list of integers. The arrow in `-> int` describes the returned value. A union such as `int | None` means the result may be an integer or `None`, which often represents a missing answer. Hints describe a contract; Python does not automatically reject a wrong type because of them.

```python
def first_or_none(values: list[int]) -> int | None:
    return values[0] if values else None

print(first_or_none([17, 23]))  # 17
print(first_or_none([]))       # None
```

Our alias exercise accepts arbitrary payload objects, so it uses `Any`, imported from `typing`, instead of promising integers. `list[Any]` describes a list whose elements may have different types. The supplied `from __future__ import annotations` keeps annotations from being evaluated immediately; this will also allow classes to refer to their own type later. You are implementing behavior, not being graded on annotation spelling.

## Assignment does not copy a list

A variable holds a reference to an object. After `backup = original`, both names refer to the same object. Calling a mutating method through either name changes that object. Reassigning one name is different: it changes what that name refers to, not the other name.

```python
colors = ["ochre"]
label = colors
label.append("teal")
print(colors)                 # ['ochre', 'teal']
label = ["silver"]
print(colors)                 # ['ochre', 'teal']
```

Follow the two statements involving `label` separately. The method call follows an existing reference and changes the list. The assignment creates a different list and points only `label` at it. This distinction matters when a function receives a list: the parameter is another name referring to the caller's object.

![Before rebinding, names a and b both refer to list \[17\]. After a is rebound to \[29\], b still refers to the original list \[17\].](shared-reference-map.svg)

Rebinding `a` redirects only its arrow; `b` still refers to the original list.

## Preserve the shared object

`append_shared(items, value)` must add one value to the end of the caller's list and return that same list. The returned reference lets another caller keep sharing it. Returning `items.append(value)` would return `None`, because `append` changes its receiver but does not return the changed list. Concatenation would create a new outer list and break the identity contract.

An empty list still has identity and can still be shared. Repeated values are allowed; adding an existing value means another entry, not replacing the old entry. Each call adds exactly one reference and leaves existing positions in their original order. List append has amortized O(1) cost; a later lesson will explain why an individual append can cost more. This operation does not copy the list or the object being added.

## Build in small steps

The first check observes the list after the call and ignores the return value. Once mutation works, the second check asks whether the returned reference is that same list.

## Your Tasks

1. Append the supplied value once to `items`.
2. Return `items` itself, not the result of `append`.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
