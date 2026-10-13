from solution import *


def test_01_behavior():
    """Transform novel categories with handle_unknown='ignore' and explain the all-zero row."""
    for train in (np.array([["wood"], ["metal"], ["fabric"]]), np.array([["pan"], ["bowl"]])):
        known = train[0, 0]
        query = np.array([["unseen-a"], [known], ["unseen-b"]])
        result = encode_new(train, query)
        assert result is not None, "Return the training-fitted encoder and transformed query."
        encoder, values = result
        assert isinstance(encoder, OneHotEncoder)
        assert encoder.handle_unknown == "ignore" and encoder.drop is None and encoder.sparse_output is False
        categories = np.unique(train[:, 0])
        np.testing.assert_array_equal(encoder.categories_[0], categories)
        np.testing.assert_array_equal(values, (query == categories.reshape(1, -1)).astype(float))
        assert values.shape == (3, len(categories))
        assert not values[0].any() and not values[2].any()
        other, _ = encode_new(train, np.array([["yet-another"], [known]]))
        np.testing.assert_array_equal(other.categories_[0], categories)
