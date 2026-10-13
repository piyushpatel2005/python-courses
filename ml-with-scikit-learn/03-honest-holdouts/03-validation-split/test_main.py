from solution import *


def test_01_behavior():
    """Split the development portion again so model choices never inspect final test targets."""
    for n in (60, 80, 100):
        ids = np.arange(200, 200+n)
        result = three_way(ids)
        assert result is not None, "Return train, validation, and test IDs."
        a, b, c = result
        assert [len(a), len(b), len(c)] == [3*n//5, n//5, n//5]
        assert set(a).isdisjoint(b) and set(a).isdisjoint(c) and set(b).isdisjoint(c)
        assert set(a) | set(b) | set(c) == set(ids)
        dev, expected_test = train_test_split(ids, test_size=.2, random_state=17)
        expected_train, expected_val = train_test_split(dev, test_size=.25, random_state=17)
        for got, want in zip(result, (expected_train, expected_val, expected_test)):
            np.testing.assert_array_equal(got, want)
