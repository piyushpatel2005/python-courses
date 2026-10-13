from solution import *

def test_01_behavior():
    """Build the regression pipeline"""
    X = np.array([[1., 2., 3.], [2., 4., 6.], [np.nan, 30., 9.], [8., np.nan, 12.]])
    y = np.array([8., 14., 20., 31.])
    for alpha in (0.1, 10.):
        model = build_model(X, y, alpha)
        assert isinstance(model, Pipeline), "Return the fitted pipeline."
        assert model.named_steps["impute"].strategy == "median"
        assert np.allclose(model.named_steps["impute"].statistics_, np.nanmedian(X, axis=0))
        assert model.named_steps["scale"].n_samples_seen_ == len(X)
        assert model.named_steps["ridge"].alpha == alpha
        before = model.named_steps["scale"].mean_.copy()
        assert np.isfinite(model.predict([[np.nan, 1000., 7.], [3., 8., 10.]])).all()
        assert np.array_equal(before, model.named_steps["scale"].mean_), "Queries must reuse fitted state."

