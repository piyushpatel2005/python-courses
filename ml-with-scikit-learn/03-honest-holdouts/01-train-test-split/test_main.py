from solution import *


def test_01_behavior():
    """Split aligned row IDs X and y reproducibly before any learned preprocessing."""
    for n in (20, 40):
        ids = np.arange(100, 100+n)
        X = np.column_stack((ids * 2., ids * 3.))
        y = ids * 7.
        parts = split_rows(ids, X, y)
        assert parts is not None, "Return all six aligned partitions."
        a, b, xa, xb, ya, yb = parts
        assert len(a) == 3*n//4 and len(b) == n//4
        assert set(a).isdisjoint(b) and set(a) | set(b) == set(ids)
        for idx, features, target in ((a, xa, ya), (b, xb, yb)):
            np.testing.assert_array_equal(features[:, 0], idx * 2.)
            np.testing.assert_array_equal(features[:, 1], idx * 3.)
            np.testing.assert_array_equal(target, idx * 7.)
        expected = train_test_split(ids, X, y, test_size=.25, random_state=17)
        for got, want in zip(parts, expected):
            np.testing.assert_array_equal(got, want)
        for got, want in zip(parts, split_rows(ids, X, y)):
            np.testing.assert_array_equal(got, want)
