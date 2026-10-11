---
title: 'Demo: Follow a Dotted Package Import'
slug: packages-and-dotted-imports
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: 'Use ElementTree from a standard-library package.'
seo_title: 'Demo: Follow a Dotted Package Import | Python Basics'
seo_description: 'Use ElementTree from a standard-library package.'
seo_keywords: [python basics, packages and dotted imports, python practice]
hints:
  - Keep the import; replace the tag inside the quoted string.
---

A package organizes related modules. The dotted name `xml.etree.ElementTree` follows that organization to a module in Python's standard library. The starter imports it `as ET`: `ET` is just a shorter name for the same module.

This module reads XML, a text format with tags such as `<trail />`. `ET.fromstring(xml_text)` reads the text into an object. Its `.tag` attribute gives the name of the outermost tag, such as `trail`. You do not need to install anything for this example.

In `main.py`, change the final call's text from `<trail />` to `<beacon />`. Run should print `beacon`, then Submit.

## Your Task

1. Change the tag in the final `tag_name` call to `<beacon />`.
