---
title: "Weight text with TF-IDF"
slug: "tfidf"
order: 9
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "pandas"
  - "numpy"
  - "scikit-learn"
language: "python"
summary: "Fit TfidfVectorizer and calculate smoothed IDF then row normalization on a tiny example."
seo_title: "Weight text with TF-IDF | Scikit-learn practice"
seo_description: "Fit TfidfVectorizer and calculate smoothed IDF then row normalization on a tiny example. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "tfidf"
  - "Python practice"
---

TF-IDF downweights words that occur in many training documents. `TfidfVectorizer` combines token counting, inverse-document-frequency weighting, and row normalization. Defaults use raw term counts, smoothed IDF, and L2 normalization. Set them explicitly here so the arithmetic is visible.

Fit on the training corpus, then transform queries with the frozen vocabulary and IDF. Document frequency counts documents containing a term, not total repetitions. Repeating a word changes term frequency but does not add another document. A query containing only unknown words remains a zero row after normalization.

The output remains sparse. Inspect `idf_` alongside `get_feature_names_out()` to align weights with words. This representation captures shared tokens, not synonyms or the meaning of a sentence; a high TF-IDF weight is not a positive review label.

With $n$ training documents and document frequency $df_t$ for token $t$,

$$
idf_t=\log\frac{1+n}{1+df_t}+1.
$$

The logarithm is natural. For two documents `oak shelf` and `shelf`, $idf_{oak}=\log(3/2)+1\approx1.4055$ and $idf_{shelf}=1$. For document $d$, let $c_{dt}$ be its count of token $t$. Then the unnormalized weight is $a_{dt}=c_{dt}idf_t$. Normalize each nonzero row:

$$
x_{dt}=\frac{a_{dt}}{\sqrt{\sum_j a_{dj}^{2}}}.
$$

Here $x_{dt}$ is the normalized weight of token $t$ in document $d$, and $j$ ranges over vocabulary columns. The first row becomes approximately $[0.8148,0.5797]$ in `[oak, shelf]` order. These unitless values agree with the vectorizer on this two-document illustration. The editor uses a larger separate corpus.

![Two documents: oak shelf; shelf; IDF(oak) = 1.4055; IDF(shelf) = 1; First normalized row: [0.8148,0.5797]](tfidf-data-flow.svg)

The starter runs a comparison baseline. Change `norm=None` to `norm="l2"`.

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

1. Fit `TfidfVectorizer(max_features=100, smooth_idf=True, norm="l2")` on training text only and return its vectorizer and transformed query matrix from `encode_tfidf`.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
