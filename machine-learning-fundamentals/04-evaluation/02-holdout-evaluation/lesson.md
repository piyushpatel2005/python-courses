---
title: Holding out evaluation data
slug: holdout-evaluation
order: 2
language: python
lesson_type: informational
summary: Keep fitting, model choice, and final evaluation separate.
seo_title: Holding out evaluation data | Machine Learning Fundamentals
seo_description: Keep fitting, model choice, and final evaluation separate.
seo_keywords:
- machine learning
- holding out evaluation data
hints:
- The validation set, or suitable cross-validation on the development data. Keep the final test set
  out of that choice.
---

Separate examples let us estimate how a model behaves beyond its training records. A common design uses training, validation, and test sets.

The training set fits the model. The validation set helps choose an approach and settings, such as tree depth or the number of neighbors. These chosen settings are called **hyperparameters**. The test set supports a final check after those choices are fixed.

Repeatedly checking the test score and changing the model makes the test set part of model selection. Its score can then look better than performance on genuinely new cases. A test set is useful because it has been kept out of those decisions, not because its filename says "test."

The split should reflect the intended use. For tomorrow's deliveries, train on earlier trips and evaluate on later trips. If repeated records concern the same rider, keep a rider's related records together when the goal is to generalize to unseen riders. A random row split can otherwise make evaluation too easy.

Cross-validation repeats training and validation across several partitions to make comparisons less dependent on one split. It must still respect time or group boundaries, and it does not turn the final test set into tuning data.

Dataset size and the intended use determine appropriate split proportions; there is no universally correct percentage. A small test set produces an unstable estimate, especially for rare classes. Report its size and relevant class counts along with the score.

## Check your understanding

Which set should guide a choice between a shallow and a deep tree?

**Answer:** The validation set, or suitable cross-validation on the development data. Keep the final test set out of that choice.
