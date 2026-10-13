from solution import *


def test_01_behavior():
    """Use get_params and set_params without confusing settings with fitted attributes."""
    for positive in (False, True):
        model = LinearRegression(fit_intercept=False, positive=positive, n_jobs=1)
        result = configure(model)
        assert result is model, "Update and return the supplied estimator."
        assert result.get_params()["fit_intercept"] is True
        assert result.get_params()["positive"] is positive, "Do not replace unrelated settings."
        assert not hasattr(result, "coef_"), "Configuration should not fit data."
        result.fit(np.array([[1.], [2.], [3.]]), np.array([5., 7., 9.]))
        np.testing.assert_allclose(result.intercept_, 3., rtol=1e-7, atol=1e-8)
