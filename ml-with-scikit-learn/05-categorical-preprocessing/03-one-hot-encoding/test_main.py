from solution import *


def test_01_behavior():
    """Fit OneHotEncoder(sparse_output=False) and read get_feature_names_out."""
    for train, query in ((np.array([["wood"], ["metal"], ["fabric"]]), np.array([["wood"], ["fabric"], ["metal"], ["wood"]])), (np.array([["pan"], ["bowl"], ["mug"], ["tray"]]), np.array([["tray"], ["bowl"], ["pan"]]))):
        result = encode_categories(train, query)
        assert result is not None, "Return encoder, dense values, and names."
        encoder, values, names = result
        assert isinstance(encoder, OneHotEncoder) and encoder.sparse_output is False
        assert encoder.drop is None and encoder.handle_unknown == "error"
        categories = np.unique(train[:, 0])
        np.testing.assert_array_equal(encoder.categories_[0], categories)
        expected = (query == categories.reshape(1, -1)).astype(float)
        np.testing.assert_array_equal(values, expected)
        assert list(names) == ["category_" + c for c in categories]
        assert values.shape == (len(query), len(categories))
        np.testing.assert_array_equal(values.sum(axis=1), np.ones(len(query)))
