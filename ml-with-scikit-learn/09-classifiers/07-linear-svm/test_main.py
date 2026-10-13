from solution import *

def test_01_behavior():
    """Fit a linear support-vector classifier"""
    X = np.array([[-4., 0.], [-3., 1.], [-2., -1.], [2., 1.], [3., -1.], [4., 0.]])
    y = np.array([3, 3, 3, 8, 8, 8])
    for C in (0.2, 3.):
        m = fit_margin(X, y, C)
        assert isinstance(m, Pipeline), "Return a fitted margin pipeline."
        assert isinstance(m.named_steps["model"], LinearSVC)
        assert m.named_steps["model"].C == C and m.named_steps["model"].dual == "auto"
        q = np.array([[-10., 0.], [10., 0.]])
        score = m.decision_function(q)
        assert score.shape == (2,) and score[0] < 0 < score[1]
        assert np.array_equal(m.predict(q), m.classes_[(score > 0).astype(int)])
        assert not hasattr(m, "predict_proba"), "A margin is not a probability."
        assert np.allclose(m.named_steps["scale"].mean_, X.mean(axis=0))

