from solution import *


def test_01_behavior():
    """Use make_regression and make_classification with explicit sizes and seeds."""
    for seed, n in ((17, 80), (29, 100)):
        result = generate(seed, n)
        assert result is not None, "Return X and y from make_classification."
        X, y = result
        expected = make_classification(n_samples=n, n_features=3, n_informative=2, n_redundant=0, n_classes=2, random_state=seed)
        assert X.shape == (n, 3) and y.shape == (n,)
        assert set(y) == {0, 1}
        for actual, wanted in zip((X, y), expected):
            np.testing.assert_allclose(actual, wanted, rtol=1e-7, atol=1e-8)
        np.testing.assert_array_equal(generate(seed, n)[0], X)
    assert not np.array_equal(generate(17, 80)[0], generate(29, 80)[0])
