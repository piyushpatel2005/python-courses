---
title: "Choose an object truth value"
slug: "truthy-objects"
order: 10
language: "python"
lesson_type: "coding"
summary: "Define __bool__ from usable capacity rather than object existence."
seo_title: "Choose an object truth value | Object-oriented Python"
seo_description: "Define __bool__ from usable capacity rather than object existence. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "truthy objects", "object oriented programming"]
hints: ["Combine the enabled flag with a strict greater-than-zero comparison."]
---

# Choose an object truth value

A battery object exists even when its charge is exhausted. An `if battery` check should answer whether it can supply power, not whether Python allocated the object. Implement a truth-value policy for `Battery`.

Python uses `__bool__(self)` for explicit `bool(value)` calls and for conditions such as `if value`. Unlike many ordinary functions, this special method must return an actual `bool`: `True` or `False`. Returning the numeric charge directly is invalid even though numbers themselves have truth values. A comparison is convenient because it already produces the required boolean result.

The supplied class stores `charge` and an `enabled` switch. A battery is usable only when enabled and its charge is strictly greater than zero. Zero and negative readings should both be false. This rule describes usefulness in this small model; it does not attempt to simulate a physical battery. The initializer already converts the switch to a boolean so your method can combine it with a comparison.

The example below checks whether a shop has room for another visitor. It distinguishes existence from a domain condition in ordinary data. Your class will make that kind of decision available directly through Python's truth-testing protocol.

If `__bool__` is absent, Python can use `__len__`; if both are absent, ordinary instances are true. When both methods exist, `__bool__` takes priority. There is no reason to invent a length for a battery just to control conditions. Pick the hook that expresses the question directly.

Read the current fields on every call. Turning a battery off or changing its charge should immediately affect its truth value. The probe includes a disabled battery with positive charge to expose implementations that check only the number and forget the switch.

## A small example

```python
visitors = 12
capacity = 12
can_admit = visitors < capacity
print(bool(can_admit))
```

## Your Tasks

1. Implement `Battery.__bool__` to return true exactly when `enabled` is true and `charge` is greater than zero. The returned value must be a boolean and reflect later attribute changes.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
