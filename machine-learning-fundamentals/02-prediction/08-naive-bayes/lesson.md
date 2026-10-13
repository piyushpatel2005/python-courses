---
title: Naive Bayes
slug: naive-bayes
order: 8
language: python
lesson_type: informational
summary: See how a simple classifier combines evidence with starting frequencies.
seo_title: Naive Bayes | Machine Learning Fundamentals
seo_description: See how a simple classifier combines evidence with starting frequencies.
seo_keywords:
- machine learning
- naive bayes
hints:
- The words are related even within a message category, so treating their evidence as independent
  can overcount it.
---

A word can provide evidence about a message category without settling the classification on its own. **Naive Bayes** combines evidence from features with the starting frequency of each class.

The starting frequency is a **prior**: how common a category is before considering this message's features. The model then uses how frequently features occur within each class to compare the categories after seeing the message. Training estimates those patterns from labeled messages.

"Naive" describes its simplifying assumption: within a given class, the features are treated as conditionally independent. In plain terms, the model acts as though learning that one word occurred tells it nothing further about another word once the message category is known. Real language often breaks this assumption; "account" and "password" often occur together.

The method can still provide a useful, inexpensive text-classification baseline. Repeated or closely related evidence can make it overconfident, so a strong class prediction does not guarantee a trustworthy numerical probability. Techniques that avoid assigning zero probability to unseen feature occurrences also matter, though their implementation is outside this overview.

## Check your understanding

Why might "account" and "password" challenge the naive assumption?

**Answer:** The words are related even within a message category, so treating their evidence as independent can overcount it.
