from solution import *


def test_01_behavior():
    """Use a categorical SimpleImputer with an explicit missing marker and sentinel policy."""
    for train in (np.array([["wood"], [np.nan], ["wood"], ["metal"]], dtype=object), np.array([[np.nan], [np.nan]], dtype=object)):
        query = np.array([[np.nan], ["new-value"], ["wood"]], dtype=object)
        result = fill_categories(train.copy(), query.copy())
        assert result is not None, "Return the fitted categorical imputer and filled query."
        imputer, values = result
        assert isinstance(imputer, SimpleImputer)
        assert imputer.strategy == "constant" and imputer.fill_value == "missing"
        assert imputer.keep_empty_features is True
        np.testing.assert_array_equal(values, np.array([["missing"], ["new-value"], ["wood"]], dtype=object))
        np.testing.assert_array_equal(imputer.statistics_, ["missing"])
        assert values.shape == query.shape
