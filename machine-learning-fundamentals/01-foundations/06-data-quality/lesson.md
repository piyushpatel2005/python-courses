---
title: Data quality and coverage
slug: data-quality
language: python
lesson_type: informational
summary: Check measurements, labels, and coverage before trusting a large dataset.
seo_title: Data quality and coverage | Machine Learning Fundamentals
seo_description: Check measurements, labels, and coverage before trusting a large dataset.
seo_keywords:
- machine learning
- data quality
hints:
- No. Repetition adds no new nighttime evidence and can introduce duplicate leakage across splits.
order: 6
---

More rows do not automatically provide better evidence. Data quality includes what a row means, how it was measured, whether its target is reliable, and which situations are missing.

Start with consistency. Check units, impossible values, missing fields, duplicate records, and changes in definitions. A duration of 30 may be minutes in one source and seconds in another. A duplicate record is not a new independent example.

Next inspect coverage. A dataset containing mostly short daytime deliveries may tell us little about long overnight deliveries. A random sample from that dataset still inherits the missing coverage. The intended population matters more than the total row count.

Labels deserve the same care as features. A recorded complaint is evidence of a complaint, not a perfect measurement of dissatisfaction. Two people can apply an ambiguous labeling rule differently. Clarify the target definition and investigate systematic disagreements instead of treating all labels as unquestionable truth.

Separate known fixed corrections, such as a specified unit conversion, from preparation fitted from observed values. Any learned filling, scaling, or feature selection must use training rows only. Exploratory decisions made after looking at final test outcomes can also compromise evaluation.

Document where the examples came from, which cases are excluded, and how targets were obtained. These limitations should remain visible when interpreting model scores.

## Check your understanding

Would copying every row ten times repair missing coverage of nighttime deliveries?

**Answer:** No. Repetition adds no new nighttime evidence and can introduce duplicate leakage across splits.
