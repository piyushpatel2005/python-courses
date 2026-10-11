---
title: "Change a Gear List: Demo"
slug: change-a-playlist
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: Replace an item in a mutable gear list.
seo_title: "Change a Gear List: Demo | Python Basics"
seo_description: Replace an item in a mutable gear list.
seo_keywords: [python basics, lists and tuples, lantern atlas]
---

The loadout has a faulty lantern. A list lets you replace an item without rebuilding the whole list: `gear[0] = "Lantern"` changes the item at index zero. Strings do not allow this kind of assignment.

You can also add and remove items with list methods. Run this separate packing example and watch the list change:

```python run
pack = ["map", "snack"]
pack.append("water")
print(pack)
pack.remove("snack")
print(pack)
```

`append()` adds at the end. `remove()` removes the first matching value; `pop()` removes and returns the last item when you give it no index.

In `main.py`, the starter replaces the wrong item. Change the assignment to replace the first item, then Run and Submit.

## Your Task

1. Replace the first item in `gear` with `Lantern`.
