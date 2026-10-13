---
title: Baselines
slug: baselines
order: 4
language: python
lesson_type: informational
summary: Require a model to improve on a meaningful simple alternative.
seo_title: Baselines | Machine Learning Fundamentals
seo_description: Require a model to improve on a meaningful simple alternative.
seo_keywords:
- machine learning
- baselines
hints:
- It never warns about any of the 10 late trips. Overall correctness does not describe which mistakes
  it makes.
---

A **baseline** is a simple comparison that tells us whether a more elaborate model adds value. For delivery duration, one baseline could always predict a typical duration from the training records. For classification, it could always choose the most common training category.

Suppose an invented evaluation set contains 90 on-time trips and 10 late trips. Always predicting on time gets 90 of 100 answers right, or 90% accuracy. It also misses every late trip. A high-looking percentage can hide failure on the very cases that motivated the project.

Use the same held-out examples and the same error measures for the baseline and the candidate. An existing operational rule is another useful baseline. The candidate should justify its extra maintenance, latency, or complexity.

Baselines do not have to be intentionally weak. A simple linear model can provide a serious comparison for a complicated network. If the network does not improve outcomes enough to matter, the smaller model may be the better choice.

Decide what improvement is useful before searching through models. Otherwise model comparisons can focus on small score changes that do not improve the intended decision.

## Check your understanding

Why is the always-on-time classifier a poor late-trip warning system despite 90% accuracy?

**Answer:** It never warns about any of the 10 late trips. Overall correctness does not describe which mistakes it makes.
