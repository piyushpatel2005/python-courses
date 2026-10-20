---
title: 'Read a tag with a package import'
slug: packages-and-dotted-imports
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: 'Read the outer XML tag using a standard-library package.'
seo_title: 'Read a tag with a package import | Python Basics'
seo_description: 'Read the outer XML tag using a standard-library package.'
seo_keywords: [python package, dotted import, ElementTree]
hints:
  - Keep the import; change the tag in the final quoted string.
---

A package groups related Python modules. The dotted name `xml.etree.ElementTree` identifies the `ElementTree` module inside the standard-library `xml` package. The import uses `as ET` to give the module a shorter name in this file.

XML is text marked with tags. For example, `<order />` is an empty element whose tag name is `order`. `ET.fromstring(xml_text)` parses that text, and `.tag` reads the outer element's name. This standard-library module is already available; no extra installation is needed.

## Your Task

1. Change the text in the final `tag_name` call from `<draft />` to `<order />`.

Edit `main.py`, **Run** to see `order`, then **Submit**.
