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

# Read a Fixed Checkpoint Record: Demo

A checkpoint record keeps its marker and time together as a tuple. A tuple is ordered but fixed: assigning to `record[0]` raises `TypeError`. `marker, time = record` unpacks two values; a one-item tuple needs a comma, such as `(42,)`.

The supplied second print shows both unpacked fields. Change `marker` in `main.py` to read the first part. Run should show `Blue Beacon`, then `Checkpoint: Blue Beacon 09:00`; Submit to check.

## Your Task

1. Set `marker` to the first element of `checkpoint_record`.
