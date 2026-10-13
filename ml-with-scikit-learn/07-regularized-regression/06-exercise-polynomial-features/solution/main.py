import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge


def expand_terms(training, queries):
    transformer = PolynomialFeatures(degree=2, include_bias=False).fit(training)
    return transformer.transform(queries), transformer.get_feature_names_out()

training = np.array([[2., 5.], [4., 1.], [6., 3.], [8., 2.]])
queries = np.array([[4., 2.], [1., 5.]])

print("Expanded terms and names:", expand_terms(training, queries))
# Supplied integration example: expansion stays inside training fit.
model = Pipeline([("poly", PolynomialFeatures(2, include_bias=False)), ("scale", StandardScaler()), ("ridge", Ridge(alpha=1.))])
model.fit(training, np.array([10., 18., 17., 30.]))
print("Pipeline raw-query predictions:", model.predict(queries))
