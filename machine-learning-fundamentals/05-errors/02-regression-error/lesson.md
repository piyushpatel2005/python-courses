---
title: Measuring regression error
slug: regression-error
order: 2
language: python
lesson_type: informational
summary: Read average numerical error in the units of the task.
seo_title: Measuring regression error | Machine Learning Fundamentals
seo_description: Read average numerical error in the units of the task.
seo_keywords:
- machine learning
- measuring regression error
hints:
- Both are mistakes. Absolute values measure their sizes rather than allowing opposite directions
  to hide each other.
---

**Mean absolute error**, or MAE, averages the size of the misses without allowing early and late errors to cancel.

$$
\text{MAE}=\frac{|y_1-\hat{y}_1|+|y_2-\hat{y}_2|}{2}
$$

This version is for two trips. $y_1$ and $y_2$ are their actual times; $\hat{y}_1$ and $\hat{y}_2$ are their predicted times. The subscripts identify the trips, the hats mark predictions, and the bars mean absolute value. Dividing by 2 averages the two error sizes.

If actual times are 18 and 25 minutes and predictions are 20 and 21, the absolute errors are 2 and 4 minutes. MAE is $(2+4)/2=3$ minutes. That does not mean every trip misses by three minutes.

For more than two examples, add every absolute error and divide by the number of examples. Each example receives equal weight in this ordinary version. Compute the same measure on the same held-out rows when comparing models.

MAE retains the target's units, making it easier to interpret than an abstract score. It does not express error as a percentage: three minutes can matter differently for a five-minute prediction and a two-hour prediction. The next lesson considers squared error, which emphasizes larger misses.

Choose the measure around the decision. An average alone can hide rare, very large delays; inspect those cases separately and compare the chosen measure with the baseline.

## Check your understanding

Why should the signed misses of plus 2 and minus 4 not simply cancel when measuring error size?

**Answer:** Both are mistakes. Absolute values measure their sizes rather than allowing opposite directions to hide each other.
