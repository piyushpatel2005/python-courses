from solution import *

def test_01_behavior():
    """Fit Gaussian naive Bayes"""
    X = np.array([[1., 2.], [2., 1.], [1.5, 2.5], [6., 7.], [7., 6.], [6.5, 7.5]])
    y = np.array([2, 2, 2, 9, 9, 9])
    for priors in ([0.2, 0.8], [0.7, 0.3]):
        m = fit_bayes(X, y, priors)
        assert isinstance(m, GaussianNB), "Return fitted GaussianNB."
        assert np.allclose(m.class_prior_, priors), "Use the supplied priors in class order."
        assert np.array_equal(m.classes_, [2, 9])
        assert np.allclose(m.theta_, [X[:3].mean(axis=0), X[3:].mean(axis=0)])
        q = np.array([[1.2, 2.1], [6.8, 6.2]])
        assert np.allclose(m.predict_proba(q).sum(axis=1), 1)
        assert np.array_equal(m.predict(q), [2, 9])

