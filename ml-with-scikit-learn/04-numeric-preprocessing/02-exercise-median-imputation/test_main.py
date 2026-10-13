from solution import *


def test_01_behavior():
    """Fit SimpleImputer(strategy='median') on training columns and reuse its statistics."""
    for train in (np.array([[1., 2.], [3., np.nan], [20., 8.], [np.nan, 4.]]), np.array([[np.nan, 2.], [np.nan, 10.], [np.nan, 4.]])):
        query = np.array([[np.nan, 1000.], [7., np.nan]])
        got = fill_missing(train.copy(), query.copy())
        assert got is not None, "Return the fitted imputer and transformed query."
        imputer, values = got
        assert isinstance(imputer, SimpleImputer) and imputer.strategy == "median"
        assert imputer.keep_empty_features is True
        reference = SimpleImputer(strategy="median", keep_empty_features=True).fit(train)
        np.testing.assert_allclose(imputer.statistics_, reference.statistics_, rtol=1e-7, atol=1e-8)
        np.testing.assert_allclose(values, reference.transform(query), rtol=1e-7, atol=1e-8)
        assert np.isfinite(values).all() and values.shape == query.shape
        other, _ = fill_missing(train.copy(), query*10)
        np.testing.assert_array_equal(other.statistics_, imputer.statistics_)
