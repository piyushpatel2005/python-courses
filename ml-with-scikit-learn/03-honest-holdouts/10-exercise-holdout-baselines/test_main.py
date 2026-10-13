from solution import *


def test_01_behavior():
    """Use DummyRegressor or DummyClassifier with a task-appropriate explicitly introduced metric."""
    for target, valid in (([0, 0, 0, 1], [1, 1, 0]), ([1, 1, 1, 0], [0, 1, 0])):
        X = np.arange(4.).reshape(-1, 1)
        q = np.array([[7.], [9.], [11.]])
        result = baseline(X, np.array(target), q, np.array(valid))
        assert result is not None, "Return a fitted dummy and validation accuracy."
        model, score = result
        assert isinstance(model, DummyClassifier) and model.strategy == "most_frequent"
        majority = int(np.mean(target) > .5)
        expected = np.full(len(valid), majority)
        np.testing.assert_array_equal(model.predict(q), expected)
        np.testing.assert_allclose(score, np.mean(np.array(valid)==expected), rtol=1e-7, atol=1e-8)
        other, _ = baseline(X, np.array(target), q*100, 1-np.array(valid))
        np.testing.assert_array_equal(other.predict(q), expected)
