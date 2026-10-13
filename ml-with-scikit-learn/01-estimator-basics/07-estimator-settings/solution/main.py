import numpy as np
from sklearn.linear_model import LinearRegression


def configure(model):
    model.set_params(fit_intercept=True)
    return model


# Supplied fixture and observation probe.
X_train = np.array([[1.], [2.], [3.], [4.]])
y_train = np.array([5., 7., 9., 11.])
model = LinearRegression(fit_intercept=False, n_jobs=1)

updated = configure(model)
if updated is not None:
    print("Setting:", updated.get_params()["fit_intercept"])
    updated.fit(X_train, y_train)
    print("Learned intercept after fit:", updated.intercept_)
else:
    print("Configure the estimator before the supplied fit.")
