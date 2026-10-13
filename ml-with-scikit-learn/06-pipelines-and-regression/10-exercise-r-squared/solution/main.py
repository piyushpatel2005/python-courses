import numpy as np
from sklearn.metrics import r2_score


def relative_fit(actual, predicted):
    return r2_score(actual, predicted)

actual = np.array([10., 14., 18., 22.])
predicted = np.array([30., 30., 30., 30.])

print("R-squared:", relative_fit(actual, predicted))
