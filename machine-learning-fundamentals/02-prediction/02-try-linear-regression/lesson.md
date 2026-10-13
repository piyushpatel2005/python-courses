---
title: Try a tiny linear model
slug: try-linear-regression
order: 2
language: python
lesson_type: interactive
pyodide_packages:
- numpy
- scikit-learn
summary: Watch fit learn a line from NumPy arrays and predict one new value.
seo_title: Try a tiny linear model | Machine Learning Fundamentals
seo_description: Watch fit learn a line from NumPy arrays and predict one new value.
seo_keywords:
- machine learning
- try-linear-regression
hints:
- Follow which arrays enter fit; predict uses an already fitted model.
---

The previous lesson described a line with three additional minutes per kilometer and an eight-minute starting value. Here the model learns that relationship from four invented trips instead of receiving those two numbers directly.

This short demonstration uses familiar NumPy arrays and one model from scikit-learn. Each row of `distance` is one trip, and its single column is the distance feature. `minutes` holds the target answers in the same order. The double brackets preserve the rows-and-columns shape even though there is only one feature.

`LinearRegression()` creates an unfitted model. `fit(distance, minutes)` learns from the paired examples. `predict(...)` applies the fitted model to a new row; it does not train on that row. Press **Run** beneath the example to see the estimate.

```python run
import numpy as np
from sklearn.linear_model import LinearRegression

# Invented trips: one distance feature per row.
distance = np.array([[1.0], [2.0], [3.0], [5.0]])
minutes = np.array([11.0, 14.0, 17.0, 23.0])

model = LinearRegression()
model.fit(distance, minutes)
prediction = model.predict(np.array([[4.0]]))
print(f"Predicted minutes: {prediction[0]:.1f}")
```

The result is 20.0 minutes at four kilometers. The `.1f` formatting prints one decimal place, and `[0]` selects the only prediction in the returned array.

These invented times lie exactly on a line so that the mechanism is easy to see. The four-kilometer input is new, but this demonstration has no independent observed answer for it. It shows how fitting and prediction differ; it does not measure model quality. Later lessons introduce held-out evaluation.

Before continuing, identify the line that learns and the line that only uses what was learned. They are `fit` and `predict`, respectively.
