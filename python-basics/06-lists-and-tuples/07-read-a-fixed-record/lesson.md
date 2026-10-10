---
title: "Read a Fixed Checkpoint Record: Demo"
slug: read-a-fixed-record
order: 7
language: python
lesson_type: coding
runtime: pyodide
summary: Index and unpack an unchanging checkpoint tuple.
seo_title: "Read a Fixed Checkpoint Record: Demo | Python Basics"
seo_description: Index and unpack an unchanging checkpoint tuple.
seo_keywords: [python basics, lists and tuples, lantern atlas]
---

A checkpoint's marker and time belong together. Here they form a tuple: an ordered collection whose items you cannot replace. Assigning to `record[0]` would raise `TypeError`.

You can still read a tuple by index. You can also unpack it: `marker, time = record` assigns the first value to `marker` and the second to `time`. The number of names must match the number of values. For a one-item tuple, keep the comma: `(42,)`.

The starter already prints the unpacked fields. Change `marker` in `main.py` to read the first item. Run should show `Blue Beacon`, then `Checkpoint: Blue Beacon 09:00`. Submit to check your edit.

## Your Task

1. Set `marker` to the first element of `checkpoint_record`.
