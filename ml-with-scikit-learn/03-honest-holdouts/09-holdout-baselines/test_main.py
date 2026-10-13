from solution import *


def test_01_behavior():
    """Use DummyRegressor or DummyClassifier with a task-appropriate explicitly introduced metric."""
    for target, valid in (([2., 4., 12.], [5., 20.]), ([10., 20., 30.], [-3., 100.])):
        X = np.arange(3.).reshape(-1, 1)
        q = np.array([[7.], [9.]])
        result = baseline(X, np.array(target), q, np.array(valid))
        assert result is not None, "Return a fitted dummy and validation MAE."
        model, score = result
        assert isinstance(model, DummyRegressor) and model.strategy == "mean"
        expected = np.full(len(valid), np.mean(target))
        np.testing.assert_allclose(model.predict(q), expected, rtol=1e-7, atol=1e-8)
        np.testing.assert_allclose(score, np.mean(np.abs(np.array(valid)-expected)), rtol=1e-7, atol=1e-8)
        other, _ = baseline(X, np.array(target), q*100, np.array(valid)*100)
        np.testing.assert_allclose(other.constant_, model.constant_, rtol=1e-7, atol=1e-8)
