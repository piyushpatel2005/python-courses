from solution import *
from sklearn.datasets import make_classification

def test_01_permutation_importance():
    """Use permutation_importance on development validation data and explain correlated-feature/causality limits."""
    for seed in [11,19]:
        a,b = make_classification(n_samples=50,n_features=3,n_redundant=0,random_state=seed)
        estimator = LogisticRegression(n_jobs=1).fit(a[:35],b[:35])
        before = estimator.coef_.copy()
        result = inspect_features(estimator,a[35:],b[35:])
        assert result is not None
        expected = permutation_importance(estimator,a[35:],b[35:],scoring='accuracy',n_repeats=3,random_state=17,n_jobs=1)
        assert result.importances.shape == (3,3)
        assert np.allclose(result.importances,expected.importances,atol=1e-12)
        assert np.array_equal(before,estimator.coef_), "Do not refit during inspection."
