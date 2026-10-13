import numpy as np
from sklearn.metrics import mean_absolute_error


def error_report(actual, predicted):
    residuals = actual - predicted
    return residuals, mean_absolute_error(actual, predicted)

actual = np.array([12., 20., 28.])
predicted = np.array([10., 23., 27.])

print("Residuals and MAE:", error_report(actual, predicted))
