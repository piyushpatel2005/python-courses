---
title: Transfer learning
slug: transfer-learning
order: 7
language: python
lesson_type: informational
summary: Understand reuse of a trained model while checking whether the new setting fits.
seo_title: Transfer learning | Machine Learning Fundamentals
seo_description: Understand reuse of a trained model while checking whether the new setting fits.
seo_keywords:
- machine learning
- transfer learning
hints:
- No. Fine-tuning continues from previously learned weights.
---

**Transfer learning** reuses knowledge learned in one setting for another. An image classifier with few labeled examples can start from a model trained previously on a larger image collection instead of learning every feature from the beginning.

One option is to keep the existing model's feature-producing layers fixed and train a new output stage for the new categories. Another is **fine-tuning**: continue training some or all of the existing model's weights on the new examples.

Transfer describes reuse between settings. Self-supervision describes where a training signal comes from. A reused model might originally have learned through supervised learning or self-supervision; the terms are not interchangeable.

Reuse can reduce the amount of new training needed, but it imports assumptions from the earlier data. A model trained on bright product photos may struggle with poorly lit images from a different camera. This mismatch is a reason to test, not a reason to assume that the larger model will compensate.

Check permissions for both the model and the data, evaluate on realistic new examples, and compare with a simpler alternative. Fine-tuning does not automatically remove inherited bias or make a model's estimates reliable.

## Check your understanding

Is fine-tuning the same as training every weight from a fresh random starting point?

**Answer:** No. Fine-tuning continues from previously learned weights.
