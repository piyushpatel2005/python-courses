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

The Tool Library also reads short XML labels. A package groups modules; `xml.etree.ElementTree` is a dotted path to a standard-library module. `ET.fromstring(xml_text).tag` returns the outer tag. No installation is needed.

Edit `main.py` to change `<trail />` to `<beacon />`. **Run** to see `beacon`, then **Submit**. The next exercise checks a different XML record.

## Your Task

1. Change the tag in the final `tag_name` call to `<beacon />`.
