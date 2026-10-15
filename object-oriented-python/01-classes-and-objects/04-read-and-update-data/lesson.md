---
title: Read and update data
slug: read-and-update-data
order: 4
language: python
lesson_type: coding
summary: Complete `record_uses(item, amount)` so it adds `amount` to the existing item's `uses` attribute without replacing
  the item.
seo_title: Read and update data | Python OOP practice
seo_description: Complete `record_uses(item, amount)` so it adds `amount` to the existing item's `uses` attribute without
  replacing the item.
seo_keywords:
- Python OOP
- read and update data
- coding practice
---

# Read and update data

Each item keeps a count of its activations in `uses`. After several activations, add to that count on the existing object. Keeping the object lets any other code referring to it see the updated count.

## Read before you write

Attribute expressions work in ordinary arithmetic. This example adds steps to an existing quest record:

```python
class QuestLog:
    pass

record = QuestLog()
record.steps = 8
record.steps = record.steps + 3
print(record.steps)  # 11
```

Python evaluates the right side first. It reads the old `steps`, adds three, then stores the result back on the same object. `record.steps += 3` is a shorter way to express this update for the integer values used here.

Assigning `record.steps = 3` would replace the count with three instead of adding three. That difference is easy to miss when the initial count happens to be zero. Always try an update with a nonzero starting value as well.

A function can change an object passed to it. The parameter becomes another name for that object; it is not an automatic copy. An assignment such as `record = QuestLog()` inside the function would instead rebind the local name, leaving the caller's original object unchanged.

In this exercise, `record_uses(item, amount)` receives an already prepared item. Its job is only to increase that item's `uses` attribute by `amount`. You may assume the supplied count and amount are nonnegative integers. Validation is not part of this task.

The function does not need to return anything. The caller observes the change by reading the original object's attribute afterward. The probe records two updates on one item, which helps distinguish an accumulated count from a count that is accidentally reset on each call.

## Your Tasks

Now it’s your turn to write some code.

1. Complete `record_uses(item, amount)` so it adds `amount` to the existing item's `uses` attribute without replacing the item.

Click **Run** to inspect the results in the console, then click **Submit** when you’re done. The completed probe prints `Recorded uses: 9`.
