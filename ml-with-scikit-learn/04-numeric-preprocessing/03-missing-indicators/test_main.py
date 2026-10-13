from solution import *


def test_01_behavior():
    """Use add_indicator=True and identify columns appended from training missingness."""
    fixtures = (np.array([[1., 2.], [np.nan, 4.], [5., 8.]]), np.array([[1., np.nan], [3., 4.], [5., 8.]]), np.array([[np.nan, 2.], [3., np.nan], [5., 8.]]))
    for train in fixtures:
        query = np.array([[np.nan, 100.], [7., np.nan]])
        result = fill_with_flags(train.copy(), query.copy())
        assert result is not None, "Return an imputer with missing indicators."
        imputer, values = result
        assert isinstance(imputer, SimpleImputer) and imputer.add_indicator is True
        expected_columns = np.flatnonzero(np.isnan(train).any(axis=0))
        np.testing.assert_array_equal(imputer.indicator_.features_, expected_columns)
        assert values.shape == (2, 2+len(expected_columns))
        np.testing.assert_array_equal(values[:, 2:], np.isnan(query[:, expected_columns]).astype(float))
        reference = SimpleImputer(strategy="median", add_indicator=True, keep_empty_features=True).fit(train)
        np.testing.assert_allclose(values, reference.transform(query), rtol=1e-7, atol=1e-8)
