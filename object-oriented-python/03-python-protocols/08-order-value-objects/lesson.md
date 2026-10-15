---
title: "Order value objects"
slug: "order-value-objects"
order: 8
language: "python"
lesson_type: "coding"
summary: "Implement __lt__ for sorting without inventing unsupported comparisons."
seo_title: "Order value objects | Object-oriented Python"
seo_description: "Implement __lt__ for sorting without inventing unsupported comparisons. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "order value objects", "object oriented programming"]
hints: ["Return the comparison of the two measurements, not their difference."]
---

# Order value objects

A race report needs results in ascending elapsed time. You already know how equality differs from identity; ordering adds a different question: which value belongs earlier? Teach `RaceTime` how to answer the less-than comparison.

The expression `a < b` uses the rich comparison protocol, commonly starting with `a.__lt__(b)`. Rich comparison is the name for methods such as `__lt__`, `__eq__`, and `__ge__`. Each has its own meaning. Python does not automatically derive every ordering operator just because you implement one of them.

For this exercise, compare the stored `seconds` values and return a boolean. Equal times are not less than each other. Sorting uses less-than comparisons, so this single method is enough for `sorted(times)` to produce the requested order. `sorted` returns a new list; it does not rewrite the original list or mutate the objects.

An unrelated operand should receive `NotImplemented`. Python can try the reflected comparison: for `<`, the corresponding other-side operation is `>`, rather than a method named `__rlt__`. If neither side supports ordering, the expression raises `TypeError`. This is deliberate; arbitrary object identities do not provide a useful race order. The guarded probe keeps unfinished work from stopping Run, while the tests inspect both supported comparisons and the declined path.

The example sorts built-in numbers representing oven temperatures. Those numbers already implement ordering. Your task supplies a comparable behavior for an object that carries its number in an attribute.

Keep equality separate. We are not requiring a complete ordering library here, and you should not add `<=` or compare the human-readable labels. A later application may need tie-breaking fields; this contract says seconds alone determine whether one result is earlier.

## A small example

```python
temperatures = [210, 180, 200]
ordered = sorted(temperatures)
print(ordered)
print(temperatures)
```

## Your Tasks

1. Implement `RaceTime.__lt__` using `seconds`, returning `NotImplemented` for non-`RaceTime` operands. Sorting must preserve the objects and order them by increasing seconds; equal times are not less than each other.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
