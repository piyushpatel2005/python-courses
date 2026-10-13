from solution import *

def test_01_behavior():
    """Exercise: shrink coefficients with Ridge"""
    X = np.array([[1., 2.], [2., 4.1], [3., 6.], [5., 10.2], [8., 16.]])
    y = np.array([3., 5., 6., 11., 15.])
    for alpha in (0.2, 12.):
        m = fit_ridge(X, y, alpha)
        assert isinstance(m, Pipeline), "Return the fitted scaled Ridge pipeline."
        assert isinstance(m.named_steps["ridge"], Ridge)
        assert m.named_steps["ridge"].alpha == alpha, "Use the supplied alpha."
        assert np.allclose(m.named_steps["scale"].mean_, X.mean(axis=0))
        expected = Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=alpha))]).fit(X, y)
        q = np.array([[4., 8.], [9., 18.]])
        assert np.allclose(m.predict(q), expected.predict(q), atol=1e-7)

