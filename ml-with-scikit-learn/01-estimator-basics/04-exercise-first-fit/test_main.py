from solution import *


def test_01_behavior():
    """Fit LinearRegression on supplied training-only observations and distinguish learned attributes from constructor settings."""
    for offset, slope in ((3., 2.), (-4., 1.5)):
        X = np.array([[1.], [2.], [4.], [7.]])
        y = offset + slope * X[:, 0]
        model = fit_line(X, y)
        assert isinstance(model, LinearRegression), "Return a fitted LinearRegression."
        assert model.get_params()["fit_intercept"] is True
        np.testing.assert_allclose(model.coef_, [slope], rtol=1e-7, atol=1e-8)
        np.testing.assert_allclose(model.intercept_, offset, rtol=1e-7, atol=1e-8)
        assert model.n_features_in_ == 1
