from solution import *


def test_01_behavior():
    """Calculate StandardScaler training mean and population scale and transform a query."""
    for train in (np.array([[2., 5.], [4., 5.], [6., 5.]]), np.array([[10., 1.], [20., 3.], [50., 7.], [80., 11.]])):
        query = np.array([[8., 5.], [100., 9.]])
        result = standardize(train.copy(), query.copy())
        assert result is not None, "Return the fitted StandardScaler and transformed queries."
        scaler, values = result
        assert isinstance(scaler, StandardScaler) and scaler.with_mean and scaler.with_std
        mean, std = train.mean(axis=0), train.std(axis=0, ddof=0)
        scale = np.where(std == 0, 1., std)
        np.testing.assert_allclose(scaler.mean_, mean, rtol=1e-7, atol=1e-8)
        np.testing.assert_allclose(scaler.scale_, scale, rtol=1e-7, atol=1e-8)
        np.testing.assert_allclose(values, (query-mean)/scale, rtol=1e-7, atol=1e-8)
        other, _ = standardize(train.copy(), query*100.)
        np.testing.assert_allclose(other.mean_, mean, rtol=1e-7, atol=1e-8)
