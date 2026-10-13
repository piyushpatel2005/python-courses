import numpy as np
from sklearn.linear_model import LinearRegression


def fit_line(X_train, y_train):
    model = LinearRegression(fit_intercept=True, n_jobs=1)
    model.fit(X_train, y_train)
    return model


# Supplied fixture and observation probe.
X_train = np.array([[1.], [2.], [3.], [4.]])
y_train = np.array([5., 7., 9., 11.])

model = fit_line(X_train, y_train)
if model is not None:
    print("coefficient:", model.coef_)
    print("intercept:", model.intercept_)
else:
    print("Fit the supplied training observations.")
