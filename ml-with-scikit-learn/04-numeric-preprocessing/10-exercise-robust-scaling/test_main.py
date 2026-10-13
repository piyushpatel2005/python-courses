from solution import *


def test_01_behavior():
    """Compare RobustScaler median/IQR with standard scaling on training outliers."""
    for train in (np.array([[2.], [4.], [6.], [8.], [100.]]), np.array([[10., 2.], [20., 4.], [30., 6.], [40., 8.], [400., 100.]])):
        query = train[[1, -1]] + 3.
        result = robust_scale(train.copy(), query.copy())
        assert result is not None, "Return a fitted RobustScaler and query values."
        scaler, values = result
        assert isinstance(scaler, RobustScaler)
        assert tuple(scaler.quantile_range) == (25, 75)
        center = np.median(train, axis=0)
        q1, q3 = np.percentile(train, [25, 75], axis=0)
        np.testing.assert_allclose(scaler.center_, center, rtol=1e-7, atol=1e-8)
        np.testing.assert_allclose(scaler.scale_, q3-q1, rtol=1e-7, atol=1e-8)
        np.testing.assert_allclose(values, (query-center)/(q3-q1), rtol=1e-7, atol=1e-8)
        assert values.shape == query.shape
        other, _ = robust_scale(train.copy(), query*100.)
        np.testing.assert_array_equal(other.center_, center)
