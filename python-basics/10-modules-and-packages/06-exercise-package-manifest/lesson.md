---
title: 'Exercise: Read an Atlas Record'
slug: exercise-package-atlas
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: 'Use a dotted import to recognize an atlas XML root.'
seo_title: 'Exercise: Read an Atlas Record | Python Basics'
seo_description: 'Use a dotted import to recognize an atlas XML root.'
seo_keywords: [python package exercise, dotted import, ElementTree]
hints:
  - Import xml.etree.ElementTree as ET, then inspect the parsed root's tag.
---

Check whether a Tool Library record has an `atlas` root. The root is the outermost XML tag: in `<atlas><beacon /></atlas>`, it is `atlas`, not `beacon`. Looking for the word anywhere in the text would not be enough.

Use the same standard-library module as the demo. Edit `main.py` to import it and complete the check. Run should print `True` for the supplied example, then Submit.

## Your Tasks

1. Import `xml.etree.ElementTree` as `ET`.
2. Complete `is_atlas(xml_text)` to parse the text with `ET.fromstring` and return whether its root tag is `"atlas"`.
