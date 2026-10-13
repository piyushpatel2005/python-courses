import numpy as np
from sklearn.metrics import root_mean_squared_error, mean_absolute_error


def rmse_value(actual, predicted):
    return root_mean_squared_error(actual, predicted)

actual = np.array([10., 20., 30., 40.])
predicted = np.array([10., 20., 30., 46.])

print("RMSE:", rmse_value(actual, predicted))
print("MAE:", mean_absolute_error(actual, predicted))
