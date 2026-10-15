---
title: Constructor defaults
slug: constructor-defaults
order: 10
language: python
lesson_type: coding
summary: Change the `Tool` initializer so `uses` defaults to `0` when omitted, while explicit positional or keyword counts
  are preserved.
seo_title: Constructor defaults | Python OOP practice
seo_description: Change the `Tool` initializer so `uses` defaults to `0` when omitted, while explicit positional or keyword
  counts are preserved.
seo_keywords:
- Python OOP
- constructor defaults
- coding practice
---

# Constructor defaults

New tools usually have no recorded uses. Let callers omit that count while keeping the option to import an older tool with an explicit count. This is an ordinary default argument applied to an initializer.

## Optional arguments still become instance data

```python
class Bookmark:
    def __init__(self, title, page=1):
        self.title = title
        self.page = page

start = Bookmark("Field notes")
later = Bookmark("Recipes", page=24)
```

The first call omits `page`, so its parameter receives `1`. The second call supplies a keyword argument, so it receives `24`. Both calls still execute the same assignment to `self.page`.

Required parameters come before optional parameters in this signature. Keep `self` first, even though callers do not pass it explicitly. The caller can supply the optional value positionally or by keyword; its parameter name becomes part of that calling interface.

A parameter default is not a class attribute. In the earlier class-default lesson, an instance read could fall back to data stored on the class. Here the initializer uses a default argument and then stores a separate attribute on every new instance. Changing one instance's page does not change what a future call will receive.

Immutable values such as the integer used here make uncomplicated defaults. A list as a default argument can accidentally be shared across calls; the next lesson will put a fresh list inside the initializer instead.

The editor contains a working initializer whose `uses` argument is still required. Your change belongs in its signature, not in the assignments. Do not replace every supplied count with zero: imported tools must keep their history. The probe deliberately constructs one new tool and one used tool, so you can observe both paths after a single edit.

## Your Tasks

1. Change the `Tool` initializer so `uses` defaults to `0` when omitted, while explicit positional or keyword counts are preserved.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe reports `0` for the new tool and `6` for the imported one.
