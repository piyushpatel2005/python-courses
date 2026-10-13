from solution import *

def test_01_behavior():
    """Produce sparse coefficients with Lasso"""
    rng = np.random.default_rng(7)
    X = rng.normal(size=(40, 3)); y = 4*X[:, 0] - 2*X[:, 1] + rng.normal(size=40)*0.1
    for alpha in (0.3, 3.):
        m = fit_lasso(X, y, alpha)
        assert isinstance(m, Pipeline), "Return a fitted pipeline."
        est = m.named_steps["lasso"]
        assert isinstance(est, Lasso) and est.alpha == alpha, "Use Lasso with the requested alpha."
        assert np.allclose(m.named_steps["scale"].mean_, X.mean(axis=0))
        reference = Pipeline([("scale", StandardScaler()), ("lasso", Lasso(alpha=alpha, max_iter=5000, tol=1e-6))]).fit(X, y)
        assert np.allclose(m.predict(X[:4]+0.3), reference.predict(X[:4]+0.3), atol=1e-4)

