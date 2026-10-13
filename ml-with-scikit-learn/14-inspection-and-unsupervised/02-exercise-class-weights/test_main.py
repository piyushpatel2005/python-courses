from solution import *

def test_01_class_weights():
    """Use class_weight='balanced' and compare validation errors without resampling the test set."""
    for labels in [np.array([0]*8+[1]*4), np.array([0]*5+[1]*7)]:
        values = np.column_stack([np.arange(12), np.arange(12)%3])
        model = fit_weighted(values, labels)
        assert model is not None, "Return the fitted model."
        assert model.class_weight == "balanced", "Balance using training labels."
        assert model.n_jobs == 1
        expected = LogisticRegression(class_weight="balanced", max_iter=300, n_jobs=1).fit(values, labels)
        assert np.allclose(model.predict_proba(values), expected.predict_proba(values), atol=1e-7)
        weights = compute_class_weight('balanced', classes=np.unique(labels), y=labels)
        assert np.allclose(weights * np.bincount(labels), len(labels)/2)
