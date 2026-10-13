from solution import *


def test_01_behavior():
    """Fit a supplied scaler on training rows only and transform validation rows."""
    train = np.array([[2., 10.], [4., 20.], [6., 30.]])
    for validation in (np.array([[8., 40.]]), np.array([[10000., -2000.], [8000., 4000.]])):
        got = scale_holdout(train.copy(), validation.copy())
        assert got is not None, "Return the training-fitted scaler and validation transform."
        scaler, values = got
        assert isinstance(scaler, StandardScaler)
        np.testing.assert_allclose(scaler.mean_, train.mean(axis=0), rtol=1e-7, atol=1e-8)
        np.testing.assert_allclose(scaler.scale_, train.std(axis=0), rtol=1e-7, atol=1e-8)
        assert scaler.n_samples_seen_ == len(train)
        np.testing.assert_allclose(values, (validation-train.mean(axis=0))/train.std(axis=0), rtol=1e-7, atol=1e-8)
