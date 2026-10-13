from solution import *

def test_01_behavior():
    """Compose preprocessing and prediction"""
    for shift in (0., 20.):
        frame = pd.DataFrame({"size": [1.+shift, np.nan, 5.+shift, 9.+shift], "material": ["a", "b", "a", "b"]})
        model = fit_prices(frame, np.array([5., 8., 12., 18.]))
        assert isinstance(model, Pipeline), "Fit the complete pipeline."
        branch = model.named_steps["prepare"].named_transformers_["numeric"]
        assert np.allclose(branch.named_steps["fill"].statistics_, [5.+shift]), "Learn the median from training, not zero-filled rows."
        assert branch.named_steps["scale"].n_samples_seen_ == 4
        before = branch.named_steps["scale"].mean_.copy()
        query = pd.DataFrame({"size": [1000., np.nan], "material": ["new", "a"]})
        assert np.isfinite(model.predict(query)).all()
        assert np.array_equal(branch.named_steps["scale"].mean_, before), "Prediction must not refit preprocessing."

