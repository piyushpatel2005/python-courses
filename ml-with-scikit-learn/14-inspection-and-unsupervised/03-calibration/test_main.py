from solution import *
from sklearn.datasets import make_classification

def test_01_calibration():
    """Use CalibratedClassifierCV with sigmoid and disjoint calibration folds and read reliability bins."""
    for seed in [23, 31]:
        a, b = make_classification(n_samples=48, n_features=3, n_redundant=0, random_state=seed)
        model = fit_calibrated(a, b)
        assert isinstance(model, CalibratedClassifierCV)
        assert model.method == 'sigmoid' and model.ensemble is True
        assert len(model.calibrated_classifiers_) == 3
        assert model.n_jobs == 1
        probabilities = model.predict_proba(a[:7])
        assert probabilities.shape == (7, 2)
        assert np.all((probabilities >= 0) & (probabilities <= 1))
        assert np.allclose(probabilities.sum(axis=1), 1)
        for train, calibration in model.cv.split(a,b):
            assert not set(train) & set(calibration)
