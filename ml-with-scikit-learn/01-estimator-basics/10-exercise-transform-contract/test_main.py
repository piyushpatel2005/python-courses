from solution import *


def test_01_behavior():
    """Use a supplied training-only StandardScaler to trace fit_transform and transform without relearning statistics."""
    for X in (np.array([[2.], [4.], [6.]]), np.array([[1., 10.], [3., 20.], [5., 30.]])):
        scaler = StandardScaler().fit(X)
        mean, scale = scaler.mean_.copy(), scaler.scale_.copy()
        for query in (X[:2] + 20., X + 100.):
            result = apply_scaler(scaler, query)
            assert result is not None, "Transform the query with existing state."
            np.testing.assert_allclose(result, (query - mean) / scale, rtol=1e-7, atol=1e-8)
            np.testing.assert_array_equal(scaler.mean_, mean)
            np.testing.assert_array_equal(scaler.scale_, scale)
