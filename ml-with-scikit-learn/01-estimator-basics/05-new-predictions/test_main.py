from solution import *


def test_01_behavior():
    """Predict on a new two-dimensional feature matrix with the fitted estimator."""
    for offset in (3., 11.):
        X = np.array([[1.], [2.], [4.], [6.]])
        model = LinearRegression(n_jobs=1).fit(X, offset + 2 * X[:, 0])
        old_coef = model.coef_.copy()
        for query in (np.array([[5.], [7.]]), np.array([[2.], [3.], [8.]])):
            result = predict_rows(model, query)
            assert result is not None, "Return one prediction per query row."
            assert np.asarray(result).shape == (len(query),)
            np.testing.assert_allclose(result, offset + 2 * query[:, 0], rtol=1e-7, atol=1e-8)
            np.testing.assert_array_equal(model.coef_, old_coef)
