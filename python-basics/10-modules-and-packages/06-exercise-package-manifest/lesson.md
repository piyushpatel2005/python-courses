---
title: 'Exercise: Check an invoice tag'
slug: exercise-package-atlas
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: 'Check the outer XML tag with a dotted package import.'
seo_title: 'Exercise: Check an invoice tag | Python Basics'
seo_description: 'Check the outer XML tag with a dotted package import.'
seo_keywords: [python package exercise, dotted import, ElementTree]
hints:
  - Import xml.etree.ElementTree as ET, then compare the parsed root tag.
---

A program receives a small XML record and needs to know whether its outer tag is `invoice`. In `<invoice><line /></invoice>`, the outer tag is `invoice`; in `<order><invoice /></order>`, it is `order`. Looking for the word `invoice` anywhere in the text would give the wrong answer for the second record.

Use the standard-library module from the previous lesson. `ET.fromstring(xml_text)` parses the text; `.tag` gives you the outer tag to compare. The starter supplies the sample record, and the tests also try other tags.

## Your Tasks

1. Import `xml.etree.ElementTree` as `ET`.
2. Complete `is_invoice(xml_text)` to parse the text with `ET.fromstring` and return whether the root tag is `"invoice"`.

Edit `main.py`, **Run** to see `True` for the supplied record, then **Submit**.
