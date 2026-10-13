---
title: Try a held-out classifier
slug: try-held-out-classification
order: 6
language: python
lesson_type: interactive
pyodide_packages:
- numpy
- scikit-learn
summary: Train a small tree on one array and count errors on separate examples.
seo_title: Try a held-out classifier | Machine Learning Fundamentals
seo_description: Train a small tree on one array and count errors on separate examples.
seo_keywords:
- machine learning
- try-held-out-classification
hints:
- Follow which arrays enter fit; predict uses an already fitted model.
---

Use a shallow decision tree to predict whether a trip will be late. The feature is distance in kilometers. The target labels are `0` for on time and `1` for late. These small arrays are invented to expose both a false alarm and a missed delay, not to imitate a realistic delivery dataset.

The training and evaluation rows are already separate. Only the training arrays go into `fit`. `max_depth=1` permits one question, and `random_state=7` fixes the random seed so repeated runs use the same random choices. Neither setting was selected by trying alternatives on these test rows.

Press **Run** to fit the tree, predict the held-out rows, and compare predictions with their known labels.

```python run
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

# Invented training trips: distance (km), then late label.
train_distance = np.array([[1.0], [2.0], [3.0], [6.0], [7.0], [8.0]])
train_late = np.array([0, 0, 0, 1, 1, 1])

# Separate invented evaluation trips; never passed to fit.
test_distance = np.array([[2.5], [4.0], [5.0], [7.5]])
test_late = np.array([0, 1, 0, 1])

model = DecisionTreeClassifier(max_depth=1, random_state=7)
model.fit(train_distance, train_late)
predicted = model.predict(test_distance)
print("Predicted labels:", predicted.tolist())
print("Actual labels:", test_late.tolist())
print("Matrix rows=actual, columns=predicted:")
print(confusion_matrix(test_late, predicted, labels=[0, 1]))
print(f"Accuracy: {(predicted == test_late).mean():.2f}")
```

The predictions are `[0, 0, 1, 1]`. The 4-kilometer trip is a missed late trip; the 5-kilometer trip is a false alarm. The other two are correct. Accuracy is 0.50, or 50%.

`confusion_matrix` counts actual labels by row and predicted labels by column. `labels=[0, 1]` puts on time first, unlike the late-first diagram in the earlier confusion-matrix lesson. Read the labels rather than memorizing a corner of the matrix. Here every cell contains one trip.

The final expression compares each prediction with its answer. NumPy averages the true/false matches as ones and zeros. There is no parameter fitting in that comparison.

Four test cases cannot establish real-world quality. If you used these errors to choose a different depth, these rows would become validation data and you would need a fresh final test set. This demonstration checks the evaluation procedure, not whether distance alone is a good warning system.
