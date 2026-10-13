from solution import *


def test_01_behavior():
    """Read Bunch data target feature_names and target_names and select aligned rows."""
    for bundle in (load_iris(), load_wine()):
        for rows in (np.array([0, 60, 140]), np.array([130, 2, 77, 44])):
            result = select_bundle(bundle, rows)
            assert result is not None, "Return X, y, feature names, and target names."
            X, y, names, classes = result
            np.testing.assert_array_equal(X, bundle.data[rows])
            np.testing.assert_array_equal(y, bundle.target[rows])
            assert list(names) == list(bundle.feature_names)
            assert list(classes) == list(bundle.target_names)
            assert X.shape[1] == len(names)
