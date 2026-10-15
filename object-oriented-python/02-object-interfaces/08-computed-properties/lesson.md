---
title: Computed properties
slug: computed-properties
order: 8
language: python
lesson_type: coding
summary: Add a read-only `ToolBatch.available` property that returns the current `total` minus `loaned`, calculating the value
  on every access.
seo_title: Computed properties | Python OOP practice
seo_description: Add a read-only `ToolBatch.available` property that returns the current `total` minus `loaned`, calculating
  the value on every access.
seo_keywords:
- Python OOP
- computed properties
- coding practice
---

# Computed properties

The workshop tracks how many items in a batch are available to lend. Store the total and the number currently loaned; calculate the remaining count when someone asks for it. A third stored counter would be easy to forget during an update.

## Derive rather than duplicate

```python
class Journey:
    def __init__(self, planned, completed):
        self.planned = planned
        self.completed = completed

    @property
    def remaining(self):
        return self.planned - self.completed
```

The getter reads two ordinary instance attributes and returns their difference. There is no `self.remaining` assignment in the initializer. Changing `completed` automatically affects the next reading because the calculation runs again.

A property does not cache its result by default. If you read it twice, the getter executes twice. That is useful here because the calculation is cheap and the source values may change between reads. Storing the result once would make sense only if you deliberately wanted a snapshot rather than a current view.

Keep one source of truth for each fact. In the journey example, planned and completed distance are stored facts; remaining distance is derived from them. Updating a derived counter separately would create opportunities for contradictory state, such as totals that no longer agree.

For the exercise, each batch's `total` and `loaned` instance attributes are the supplied stored facts. Assume they are nonnegative integers with `loaned` no greater than `total`. You do not need to reject invalid input or clamp a negative result. Those would be different contracts and could hide a mistake in the source data.

Add the `available` property yourself, including its decorator and getter. The probe changes `loaned` between reads. Leave that change in place: a correct first number alone cannot distinguish a live computation from a value copied during initialization. Submit also checks an empty batch and two separate batches to keep the calculation tied to the receiving instance.

## Your Tasks

1. Add a read-only `ToolBatch.available` property that returns the current `total` minus `loaned`, calculating the value on every access.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe reports `7`, then `4`.
