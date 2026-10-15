---
title: "Customize formatted output"
slug: "custom-format"
order: 13
language: "python"
lesson_type: "coding"
summary: "Implement a small __format__ language with explicit invalid-spec handling."
seo_title: "Customize formatted output | Object-oriented Python"
seo_description: "Implement a small __format__ language with explicit invalid-spec handling."
seo_keywords: ["python", "custom format", "object oriented programming"]
hints: ["Handle the empty specification explicitly before rejecting unknown options."]
---

# Customize formatted output

The map interface needs a compact trail distance in one label and a longer version in another. Give `TrailDistance` two formatting options without changing its stored metres. These are returned strings, not rendered graphics.

`format(value, spec)` calls `value.__format__(spec)`. An f-string also passes the text after its colon as the format specification: `f"{value:long}"` sends `"long"`. The specification is a string interpreted by the object's class. Numeric types support a large formatting language, but your class can define a small, documented set of choices instead.

The method must return a string. This exercise supports the empty specification and `short` as the compact form, and `long` as the expanded form. The empty string matters because `format(distance)` and `f"{distance}"` pass no explicit option. Do not accidentally make the default path return `None`.

Reject unknown specifications by raising `ValueError` with a useful message. `raise` stops the current operation and reports an exception; `ValueError` says the argument has the right general kind but an unacceptable value. Here the argument is a string, but its contents are not a supported option. This local use is enough for the task; the later errors module teaches broader handling. `NotImplemented` is not the unsupported-format protocol and must not be returned here.

The example formats a built-in floating-point reading. Its specification has meaning because the numeric type implements it. Your custom options will have their own spelling and results, not automatic access to all numeric format codes.

Do not replace or round the stored measurement while formatting. Display choices are views of the same object. The probe requests both views from one distance; Submit adds an unsupported option to confirm that a misspelling is reported instead of silently selecting a default.

## A small example

```python
reading = 8.125
print(format(reading, ".2f"))
print(f"{reading:.1f}")
```

## Your Tasks

1. Implement `TrailDistance.__format__`: empty spec or `short` returns `<metres> m`; `long` returns `<metres> metres`; any other spec raises `ValueError`. Do not modify `metres`.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
