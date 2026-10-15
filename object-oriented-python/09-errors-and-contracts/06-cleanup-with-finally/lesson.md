---
title: Release a resource with finally
slug: cleanup-with-finally
order: 6
language: python
lesson_type: coding
summary: Close a supplied reader after either a successful read or a failed one.
seo_title: Release a resource with finally | Python OOP practice
seo_description: Close a supplied reader after either a successful read or a failed
  one.
seo_keywords:
  - Python
  - cleanup with finally
  - object oriented programming
hints:
  - Return inside try and close inside finally.
---

# Release a resource with finally

Close a supplied reader after either a successful read or a failed one.

A `finally` block runs when control leaves its `try` block, including when a return value is ready or an exception is travelling to the caller. Put cleanup there instead of duplicating it in each path. Do not return from `finally`: that can replace the result or suppress the error. The fixture is an in-memory object, not a file or a network connection.

The test reader counts close calls, so closing once in the success path and again in finally is not correct. You only need one cleanup site. Assume close itself succeeds in this exercise; handling a cleanup failure would need an additional policy about which error to report.

## A smaller example

The event list records cleanup after the work finishes.

```python
events = []
try:
    events.append("work")
finally:
    events.append("cleanup")
print(events)
```

## Your Tasks

1. Implement `read_and_close(reader)` to return `reader.read()` and always call `reader.close()` exactly once in a `finally` block. A read error must still propagate.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. A finished probe shows the chapter followed by `Closed: True`. Press **Submit** to check the behavior with other inputs.
