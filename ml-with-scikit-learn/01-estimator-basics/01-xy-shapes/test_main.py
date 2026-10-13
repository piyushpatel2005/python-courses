from solution import *


def test_01_behavior():
    """Construct X as samples by features and y as one target per row."""
    for rows in (np.array([[1., 4., 5.], [2., 7., 7.]]), np.arange(21.).reshape(7, 3)):
        result = make_xy(rows.copy())
        assert result is not None, "Return X and y."
        X, y = result
        assert X.shape == (len(rows), 2), "Keep both feature columns, not the target."
        assert y.shape == (len(rows),)
        np.testing.assert_array_equal(X, rows[:, :2])
        np.testing.assert_array_equal(y, rows[:, 2])
