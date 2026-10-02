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

Ari checks whether the final Tool Library record is an atlas. The root is the outermost XML tag: `<atlas><beacon /></atlas>` has root `atlas`, not `beacon`. Use the standard-library package from the demo; no download or device file is needed.

Edit `main.py`, **Run** to see `True`, then **Submit**.

## Your Tasks

1. Import `xml.etree.ElementTree` as `ET`.
2. Complete `is_atlas(xml_text)` to parse the text with `ET.fromstring` and return whether its root tag is `"atlas"`.

Ari has a reusable tool for validating the atlas record and can leave the Tool Library.
