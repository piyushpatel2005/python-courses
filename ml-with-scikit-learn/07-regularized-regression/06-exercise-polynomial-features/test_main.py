from solution import *

def test_01_behavior():
    """Exercise: expand a feature representation"""
    train = np.array([[1., 4.], [3., 2.], [5., 6.]])
    for q in (np.array([[4., 2.], [1., 5.]]), np.array([[-2., 3.], [0., -1.]])):
        got = expand_terms(train, q)
        assert got is not None, "Return expanded rows and feature names."
        values, names = got
        a, b = q[:, 0], q[:, 1]
        assert np.asarray(values).shape == (len(q), 5), "Degree two needs five columns for two inputs."
        assert np.allclose(values, np.column_stack([a, b, a*a, a*b, b*b])), "Include both squares and the interaction, without a ones column."
        assert list(names) == ["x0", "x1", "x0^2", "x0 x1", "x1^2"]

