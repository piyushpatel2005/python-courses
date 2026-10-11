---
title: "Read the default index"
slug: read-a-default-index
order: 4
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Distinguish default Series labels from the values beside them."
seo_title: "Read the default index | Pandas for beginners"
seo_description: "Distinguish default Series labels from the values beside them."
seo_keywords: ["pandas", "Python data analysis", "series default integer index"]
---

The receipt totals are `5`, `8`, and `7`. The numbers `0`, `1`, and `2` printed to their left are labels, not additional receipts. When you build a Series from a list without `index=`, pandas supplies these consecutive labels starting at zero.

You can inspect just the labels with `receipts.index`. This is an Index object, which stores the labels separately from the values. Later, custom labels may no longer match positions, so it helps to keep the two ideas separate now.

## Your Task

1. Change the last value in `receipts` from `7` to `10`, keeping the automatically supplied index.

Edit `main.py` and **Run**. The last row should read label `2`, value `10`; the labels should not change. **Submit** checks both the counts and the default index.
