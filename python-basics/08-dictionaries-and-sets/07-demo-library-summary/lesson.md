---
title: "Summarize library loans"
slug: demo-library-summary
order: 7
language: python
lesson_type: coding
runtime: pyodide
summary: "Combine a list of records, book counts, and unique borrowers."
seo_title: "Summarize library loans | Python Basics"
seo_description: "Combine a list of records, book counts, and unique borrowers."
seo_keywords: [python basics, python collections, beginner python]
---

A library's loan log is a list of dictionaries. Each entry records a `member` and a `book`; the list keeps every loan, including two loans by the same person. In `main.py`, the supplied loop collects member names and counts loans by book with `book_counts.get(book, 0) + 1`. The first loan for a book starts at zero and becomes one; a later loan raises its count.

The final calculation currently counts loans rather than distinct members. Change only that calculation to count unique borrowers. **Run** should show `2 members` rather than `3`; then **Submit**.

## Your Task

1. Set `borrowers` to the number of distinct names in `members`.
