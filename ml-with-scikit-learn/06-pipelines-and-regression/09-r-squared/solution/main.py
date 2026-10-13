import numpy as np
from sklearn.metrics import r2_score


def relative_fit(actual, predicted):
    return r2_score(actual, predicted)

actual = np.array([2., 4., 6.])
predicted = np.array([8., 8., 8.])

print("R-squared:", relative_fit(actual, predicted))
