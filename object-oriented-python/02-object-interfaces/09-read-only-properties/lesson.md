---
title: Read-only properties
slug: read-only-properties
order: 9
language: python
lesson_type: coding
summary: Add a getter-only `GameItem.asset_code` property returning `_asset_code`; assigning to `asset_code` must raise `AttributeError`
  and leave the stored code unchanged.
seo_title: Read-only properties | Python OOP practice
seo_description: Add a getter-only `GameItem.asset_code` property returning `_asset_code`; assigning to `asset_code` must raise
  `AttributeError` and leave the stored code unchanged.
seo_keywords:
- Python OOP
- read-only properties
- coding practice
---

# Read-only properties

An item's asset code identifies its record even if its display name changes. Allow other code to read that code, but reject assignments through the public property. A getter-only property provides that interface.

## Read-only is an interface choice

```python
class SaveSlot:
    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        return self._number
```

The leading underscore in `_number` is a convention: it marks implementation data that callers should leave alone. It does not make the attribute secret or inaccessible. Python code can still reach it, so do not treat this as a security boundary.

The public name `number` has a getter but no setter. Reading `slot.number` returns the stored value. An assignment such as `slot.number = "changed"` raises `AttributeError` rather than silently creating an ordinary instance override. Properties have their own attribute behavior, unlike the plain class defaults from the first module.

Read-only also does not mean the entire object is immutable. Other attributes may still change, and methods could deliberately update the underlying storage. Here it simply means callers cannot assign through this one public property.

The editor stores the item's code as `_asset_code` and gives the item an ordinary editable `name`. Add a property named `asset_code` that reads the stored code. Do not add a setter or copy the code into a public instance attribute during initialization.

The probe first prints the code, then attempts to replace it inside a supplied `try`/`except AttributeError`. A rejected assignment is the expected successful behavior, not a broken Run. Submit checks that the code remains unchanged after that attempt and that the separate `name` attribute remains editable. This distinction will matter in the next lesson, where a setter allows some assignments while rejecting invalid values.

## Your Tasks

1. Add a getter-only `GameItem.asset_code` property returning `_asset_code`; assigning to `asset_code` must raise `AttributeError` and leave the stored code unchanged.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints the code and `Public reassignment rejected`.
