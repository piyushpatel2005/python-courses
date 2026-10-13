from solution import *


def test_01_behavior():
    """Use make_regression and make_classification with explicit sizes and seeds."""
    for seed, n in ((17, 80), (29, 100)):
        result = generate(seed, n)
        assert result is not None, "Return the generated X and y."
        X, y = result
        expected = make_regression(n_samples=n, n_features=2, n_informative=2, noise=3.0, random_state=seed)
        assert X.shape == (n, 2) and y.shape == (n,)
        for actual, wanted in zip((X, y), expected):
            np.testing.assert_allclose(actual, wanted, rtol=1e-7, atol=1e-8)
        again = generate(seed, n)
        np.testing.assert_array_equal(again[0], X)
        np.testing.assert_array_equal(again[1], y)
    assert not np.array_equal(generate(17, 80)[0], generate(29, 80)[0])
