---
title: Support vector machines
slug: support-vector-machines
order: 9
language: python
lesson_type: informational
summary: Understand a classifier that seeks a useful separation margin.
seo_title: Support vector machines | Machine Learning Fundamentals
seo_description: Understand a classifier that seeks a useful separation margin.
seo_keywords:
- machine learning
- support vector machines
hints:
- No. A soft-margin model permits some violations and balances them against the margin.
---

Imagine plotting parcels by two measured features and marking which were damaged. A **support vector machine**, or SVM, can seek a dividing boundary with a wide margin: space between the boundary and the closest examples from either class.

The nearby examples that constrain the boundary are called support vectors. Faraway examples often have less direct influence on its position. A wide margin can help the boundary avoid depending too closely on a few tiny variations in the data.

Real categories may overlap. A soft-margin SVM permits some boundary violations rather than insisting on perfect separation. Its settings balance a wider margin against penalties for violations. An unusual labeled example should not necessarily force an elaborate boundary.

With a kernel, an SVM can compare cases in a way that produces a curved boundary in the original features. You do not need the kernel mathematics here; the distinction is that an SVM is not restricted to a straight divider.

Feature scaling matters because distances influence the method. Large training collections can also be costly to fit. An SVM's decision score is not automatically a probability, so avoid reading a raw score as a percent chance.

## Check your understanding

If the classes overlap, must an SVM find a perfect separator?

**Answer:** No. A soft-margin model permits some violations and balances them against the margin.
