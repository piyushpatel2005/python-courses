---
title: Read and update data
slug: read-and-update-data
order: 4
language: python
lesson_type: coding
summary: Complete `record_uses(tool, amount)` so it adds `amount` to the existing tool's `uses` attribute without replacing
  the tool.
seo_title: Read and update data | Python OOP practice
seo_description: Complete `record_uses(tool, amount)` so it adds `amount` to the existing tool's `uses` attribute without
  replacing the tool.
seo_keywords:
- Python OOP
- read and update data
- coding practice
---

# Read and update data

A tool's usage count changes after a loan. Rather than replacing the whole object, update one attribute on the existing object. The supplied setup function creates tools with different starting counts.

## Read before you write

Attribute expressions work in ordinary arithmetic. This example adds pages to an existing reading record:

```python
class Reading:
    pass

record = Reading()
record.pages = 8
record.pages = record.pages + 3
print(record.pages)  # 11
```

Python evaluates the right side first. It reads the old `pages`, adds three, then stores the result back on the same object. `record.pages += 3` is a shorter way to express this update for the integer values used here.

Assigning `record.pages = 3` would replace the count with three instead of adding three. That difference is easy to miss when the initial count happens to be zero. Always try an update with a nonzero starting value as well.

A function can change an object passed to it. The parameter becomes another name for that object; it is not an automatic copy. An assignment such as `record = Reading()` inside the function would instead rebind the local name, leaving the caller's original object unchanged.

In this exercise, `record_uses(tool, amount)` receives an already prepared tool. Its job is only to increase that tool's `uses` attribute by `amount`. You may assume the supplied count and amount are nonnegative integers. Validation is not part of this task.

The function does not need to return anything. The caller observes the change by reading the original object's attribute afterward. The probe records two updates on one tool, which helps distinguish an accumulated count from a count that is accidentally reset on each call.

## Your Tasks

1. Complete `record_uses(tool, amount)` so it adds `amount` to the existing tool's `uses` attribute without replacing the tool.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `Recorded uses: 9`.
