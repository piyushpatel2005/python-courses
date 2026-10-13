import numpy as np
from sklearn.metrics import mean_absolute_error


def error_report(actual, predicted):
    residuals = actual - predicted
    return residuals, mean_absolute_error(actual, predicted)

actual = np.array([16., 35., 24., 50.])
predicted = np.array([20., 33., 29., 46.])

print("Residuals and MAE:", error_report(actual, predicted))
