---
title: Nearest neighbors
slug: nearest-neighbors
order: 4
language: python
lesson_type: informational
summary: Explain a prediction made from similar stored examples.
seo_title: Nearest neighbors | Machine Learning Fundamentals
seo_description: Explain a prediction made from similar stored examples.
seo_keywords:
- machine learning
- nearest neighbors
hints:
- Late, because two of the three neighbors have that label.
---

A **k-nearest neighbors** model, often shortened to kNN, finds the $k$ closest training examples to a new input. Here $k$ is the number of neighbors considered. For classification, a simple version takes their majority category; for regression, it averages their target values.

With distance as the only feature, two trips are close when their kilometer values are close:

$$
d=|x-a|
$$

Here $d$ is their distance in feature space, $x$ is the new trip's kilometer value, and $a$ is a stored trip's kilometer value. The vertical bars mean absolute value: ignore the sign. A 4-kilometer trip is $|4-3|=1$ kilometer away from a stored 3-kilometer trip on this feature.

If its three nearest stored trips took 17, 20, and 23 minutes, their average prediction is $(17+20+23)/3=20$ minutes. Those are invented neighbor times.

Small $k$ can make predictions sensitive to one unusual example. Larger $k$ smooths predictions but may include cases that are less relevant. With several features, scaling and the definition of distance matter. Storing examples is simple; searching a large collection at prediction time can be expensive.

The stored training features and targets are part of the fitted system. A new input has no known target when its neighbors are selected. Choosing neighbors by looking at its true target would defeat the prediction task. A distance rule also needs a policy for ties; the simple majority example assumes no tie.

## Check your understanding

For three equally weighted neighbors labeled late, on time, and late, what is the predicted category?

**Answer:** Late, because two of the three neighbors have that label.
