import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error


def select_settings(training, target, validation, actual, candidates):
    errors = []
    for degree, alpha in candidates:
        model = Pipeline([("poly", PolynomialFeatures(degree, include_bias=False)), ("scale", StandardScaler()), ("ridge", Ridge(alpha=alpha))])
        model.fit(training, target)
        errors.append(mean_absolute_error(actual, model.predict(validation)))
    return candidates[int(np.argmax(errors))], np.array(errors)

training = np.linspace(-2., 2., 18).reshape(-1, 1)
target = 10. + 3.*training[:, 0]**2
validation = np.array([[-1.7], [-0.3], [1.3]])
actual = 10. + 3.*validation[:, 0]**2
candidates = [(1, 1.), (2, 0.1), (2, 10.)]

print("Selected pair and validation MAEs:", select_settings(training, target, validation, actual, candidates))
