import numpy as np
from sklearn.linear_model import LinearRegression


def fit_line(X_train, y_train):
    model = LinearRegression(fit_intercept=True, n_jobs=1)
    model.fit(X_train, y_train)
    return model


# Supplied fixture and observation probe.
X_train = np.array([[10.], [20.], [30.], [40.], [50.]])
y_train = np.array([27., 47., 67., 87., 107.])

model = fit_line(X_train, y_train)
if model is not None:
    print("coefficient:", model.coef_)
    print("intercept:", model.intercept_)
else:
    print("Fit the supplied training observations.")
