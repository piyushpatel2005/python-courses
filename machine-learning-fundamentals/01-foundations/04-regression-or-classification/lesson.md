---
title: Regression or classification
slug: regression-or-classification
order: 4
language: python
lesson_type: informational
summary: Choose a prediction task by the kind of answer needed.
seo_title: Regression or classification | Machine Learning Fundamentals
seo_description: Choose a prediction task by the kind of answer needed.
seo_keywords:
- machine learning
- regression or classification
hints:
- Yes. The target is a numerical amount, and the size of the error matters.
---

The required output determines the prediction task.

- **Regression** predicts a numerical amount, such as delivery duration in minutes.
- **Classification** predicts a category, such as late or on time.

Classification with two possible categories is **binary classification**. With more than two mutually exclusive categories it is **multiclass classification**, such as identifying one of three package types.

A number used as a category name does not turn classification into regression. If 0 means on time and 1 means late, a prediction halfway between those labels is not a third delivery category. A model may estimate a probability between zero and one, but a separate decision rule converts it into a class.

For regression, the size of a miss matters: an estimate off by two minutes differs from one off by an hour. For classification, different wrong categories can have different consequences. Missing a late delivery and issuing an unnecessary warning are distinct errors.

A whole-number output can still be regression. Predicting tomorrow's order count concerns a numerical quantity, even though the observed count is an integer. Start with the decision and the meaning of an error, not the storage type of the target column.

## Check your understanding

Is predicting a daily order count regression even though the answer is a whole number?

**Answer:** Yes. The target is a numerical amount, and the size of the error matters.
