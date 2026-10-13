from solution import *

def test_01_behavior():
    """Select settings on validation data"""
    X = np.linspace(-2., 2., 16).reshape(-1, 1)
    q = np.array([[-1.6], [-0.2], [1.4]])
    candidates = [(1, 0.1), (2, 0.1), (2, 12.)]
    for curve in (0., 3.):
        y = 7 + 2*X[:, 0] + curve*X[:, 0]**2
        actual = 7 + 2*q[:, 0] + curve*q[:, 0]**2
        got = select_settings(X, y, q, actual, candidates)
        assert got is not None, "Return a choice and validation errors."
        choice, errors = got
        expected = []
        for degree, alpha in candidates:
            ref = Pipeline([("poly", PolynomialFeatures(degree, include_bias=False)), ("scale", StandardScaler()), ("ridge", Ridge(alpha=alpha))]).fit(X, y)
            expected.append(mean_absolute_error(actual, ref.predict(q)))
        assert np.allclose(errors, expected), "Fit each candidate only on training rows."
        assert tuple(choice) == candidates[int(np.argmin(expected))], "Choose the smallest validation MAE."

