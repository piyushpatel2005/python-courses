---
title: Class body scope
slug: class-body-scope
order: 12
language: python
lesson_type: coding
summary: Implement `AssetLabel.text(self)` to return its current `prefix` and `code` separated by a hyphen, using instance-aware
  attribute lookup so individual prefix overrides work.
seo_title: Class body scope | Python OOP practice
seo_description: Implement `AssetLabel.text(self)` to return its current `prefix` and `code` separated by a hyphen, using
  instance-aware attribute lookup so individual prefix overrides work.
seo_keywords:
- Python OOP
- class body scope
- coding practice
---

# Class body scope

A label printer uses a shared prefix unless a particular label has an override. The data is already in the right places. Your job is to read it correctly from a method without accidentally using a similarly named global variable.

## Methods need an object for attribute lookup

Names assigned in a class body become class attributes. They are not automatically local variables inside its methods. A bare name in a method follows ordinary function name lookup; Python does not search the surrounding class body as an enclosing function scope.

```python
unit = "global"

class Gauge:
    unit = "litres"

    def caption(self):
        return self.unit

print(Gauge().caption())  # litres
```

Writing `return unit` inside that method would read the module-level string `"global"`. If there were no global `unit`, it would raise `NameError`. Indenting the method inside the class does not make bare `unit` refer to `Gauge.unit`.

`self.unit` starts attribute lookup on the receiving instance, then falls back to the class for these ordinary attributes. That allows an individual gauge to override its unit. `Gauge.unit` explicitly reads the class setting instead, ignoring any instance override. Both forms have uses; choose the one matching the intended behavior.

The editor supplies a module-level `prefix`, a different class-level `prefix`, and an initializer that stores the label's code. Those deliberately conflicting values make accidental global lookup visible. The requested method must support the class default and an instance override, so read through `self`.

Keep the global value unchanged. Renaming or deleting it would hide the mistake instead of teaching the method where to look. The probe prints a default label and an overridden label. This completes the first module's model: a class defines shared behavior and defaults, while each instance can hold its own state.

## Your Tasks

1. Implement `AssetLabel.text(self)` to return its current `prefix` and `code` separated by a hyphen, using instance-aware attribute lookup so individual prefix overrides work.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `TOOL-A1` and `REPAIR-B2` after their labels.
