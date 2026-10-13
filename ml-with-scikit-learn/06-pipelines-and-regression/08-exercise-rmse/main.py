import numpy as np
from sklearn.metrics import root_mean_squared_error, mean_absolute_error


def rmse_value(actual, predicted):
    return None

actual = np.array([25., 35., 45.])
predicted = np.array([24., 36., 52.])

print("RMSE:", rmse_value(actual, predicted))
print("MAE:", mean_absolute_error(actual, predicted))
