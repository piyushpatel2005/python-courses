from solution import *

def test_01_behavior():
    """Fit logistic regression"""
    X = np.array([[-4., 1.], [-3., 2.], [-2., 1.], [2., 3.], [3., 4.], [4., 3.]])
    y = np.array([2, 2, 2, 7, 7, 7])
    for C in (0.2, 2.):
        m = fit_classifier(X, y, C)
        assert isinstance(m, Pipeline), "Return a fitted scaled classifier."
        assert isinstance(m.named_steps["model"], LogisticRegression)
        assert m.named_steps["model"].C == C
        assert np.array_equal(m.classes_, [2, 7])
        q = np.array([[-3.5, 1.], [3.5, 4.]])
        probability = m.predict_proba(q)
        assert probability.shape == (2, 2) and np.allclose(probability.sum(axis=1), 1.)
        assert np.array_equal(m.predict(q), m.classes_[np.argmax(probability, axis=1)])
        assert np.array_equal(m.predict(q), [2, 7])
        assert np.allclose(m.named_steps["scale"].mean_, X.mean(axis=0))

