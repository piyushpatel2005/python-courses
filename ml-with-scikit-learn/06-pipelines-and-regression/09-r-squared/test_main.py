from solution import *

def test_01_behavior():
    """Compare with a mean reference"""
    a = np.array([2., 4., 6.])
    for p in (a.copy(), np.full(3, 4.), np.full(3, 8.), np.array([1., 5., 7.])):
        got = relative_fit(a, p)
        assert got is not None, "Return the unbounded-below score."
        expected = 1.-np.sum((a-p)**2)/np.sum((a-a.mean())**2)
        assert np.isclose(got, expected), "Do not clip negative R-squared."

