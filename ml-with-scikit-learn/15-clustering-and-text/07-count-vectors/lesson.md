---
title: "Represent text as sparse counts"
slug: "count-vectors"
order: 7
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "pandas"
  - "numpy"
  - "scikit-learn"
language: "python"
summary: "Fit CountVectorizer on training text and inspect vocabulary sparse shape and a tiny dense slice."
seo_title: "Represent text as sparse counts | Scikit-learn practice"
seo_description: "Fit CountVectorizer on training text and inspect vocabulary sparse shape and a tiny dense slice. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "count vectors"
  - "Python practice"
---

A count matrix has one row per document and one column per learned token. `CountVectorizer` lowercases by default and splits text into word tokens of at least two characters. A repeated token increases its count; word order is lost with the default unigrams.

Call `fit` only on training documents to learn `vocabulary_`. Then `transform` counts those same columns in any new list of strings. A word appearing only in validation is ignored, not appended as a new column. `get_feature_names_out()` gives column names in matrix order. Do not assume alphabetical document order: output rows follow input document order.

The result is a SciPy sparse matrix, which stores nonzero entries rather than allocating every zero. `.toarray()` is supplied only for this tiny inspection slice. An all-unknown query has a zero row. The synthetic review snippets are original text, not customer records.

For token $t$ and document $d$, the count $c_{dt}$ is the number of occurrences of $t$ in $d$. Thus `oak oak shelf` has $c_{d,\mathrm{oak}}=2$ while `steel shelf` has zero occurrences of `oak`. Counts are nonnegative integers. The vectorizer's `oak` column reproduces these counts; row order follows the document list.

The diagram is a separate two-document arithmetic illustration, not the complete file corpus.

![Training: oak oak shelf; steel shelf; Columns: oak, shelf, steel; Counts: [2,1,0] and [0,1,1]](count-vectors-data-flow.svg)

The starter runs a comparison baseline. Fit the vocabulary on `training`, not `training + queries`.

## Dataset

Inspect `reviews.json`: 30 original training snippets and six transform-only query snippets form 36 synthetic HomeHurray records. The supplied `pd.read_json(..., orient="records", convert_dates=False)` setup reads the actual file into a DataFrame. Training/query selections remain Series until they reach the vectorizer. Each record has `review_id` (string ID, excluded from text), `text` (string), and `partition` (`train` or `query`). All text was authored for this fixed 2025-01-15 teaching snapshot. No scraped customer text is used.

`reviews.json` has **36 rows**, each representing one original text snippet.

| Column | Meaning | Type / unit | Role or availability |
|---|---|---|---|
| `review_id` | Synthetic text record ID; excluded from vocabulary | string; none | ID; excluded from vocabulary |
| `text` | Original description or review snippet | string; none | Only training text may fit vocabulary |
| `partition` | Fixed train/query assignment; never vectorized | string train/query; none | Supplied train/query boundary |

These records are original synthetic HomeHurray teaching data. Feature/ID fields are complete. Missing fields are not allowed in this fixed fixture.

The data tabs are read-only in the editor. Edit `main.py`; the file-reading setup is supplied, not an additional task.

## Your Tasks

1. Fit `CountVectorizer(max_features=100)` on `training` only, and return `(vectorizer, vectorizer.transform(queries))` from `encode_counts(training, queries)`.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
