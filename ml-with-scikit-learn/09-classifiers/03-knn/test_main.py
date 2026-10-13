from solution import *

def test_01_behavior():
    """Classify by nearest neighbors"""
    X = np.array([[0., 0.], [1., 1.], [2., 2.], [10., 10.], [11., 11.], [12., 12.]])
    y = np.array([0, 1, 1, 0, 0, 1])
    m = fit_neighbors(X, y, 3)
    assert isinstance(m, Pipeline), "Return the scaled neighbor pipeline."
    assert m.named_steps["model"].n_neighbors == 3
    assert np.allclose(m.named_steps["scale"].mean_, X.mean(axis=0))
    assert np.array_equal(m.predict([[0.1, 0.1], [11.9, 11.9]]), [1, 0]), "Use the three-neighbor majority, not the nearest label."
    shifted = fit_neighbors(X*7+30, y, 3)
    assert np.array_equal(shifted.predict(np.array([[0.1, 0.1], [11.9, 11.9]])*7+30), [1, 0])

