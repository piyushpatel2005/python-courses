---
title: "Packages and Dotted Imports"
slug: packages-and-dotted-imports
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: Use a standard-library package with a dotted import.
seo_title: "Packages and Dotted Imports | Python Basics"
seo_description: Use a standard-library package with a dotted import.
seo_keywords: [python basics, packages and dotted imports, python practice]
hints:
  - Keep the import; replace the tag inside the quoted string.
---

# Packages and Dotted Imports

A module is a `.py` file. A package groups modules under a directory, so a dotted import can reach a module inside it. Python's standard-library `xml.etree` package contains `ElementTree`; `ET.fromstring` reads a short XML tag. No package download or pip command is needed. Change the tag passed to `ET.fromstring` from `chair` to `lamp`; Run to see the new label. This is a guided edit, not a requirement to build a package in the single-file browser workspace.

## Your Tasks

1. Change the XML tag in the supplied call from `chair` to `lamp`.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.
