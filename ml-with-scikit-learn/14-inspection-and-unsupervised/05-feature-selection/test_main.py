from solution import *
from sklearn.datasets import make_classification

def test_01_feature_selection():
    """Put SelectKBest in Pipeline so selection learns only inside each fold."""
    for seed in [7, 41]:
        a,b = make_classification(n_samples=45,n_features=4,n_redundant=0,random_state=seed)
        model = fit_selected(a,b)
        assert isinstance(model, Pipeline), "Fit selection inside a Pipeline."
        selector = model.named_steps['select']
        assert isinstance(selector, SelectKBest) and selector.k == 2
        assert selector.get_support().sum() == 2
        expected = SelectKBest(f_classif,k=2).fit(a,b)
        assert np.array_equal(selector.get_support(), expected.get_support())
        assert model.predict(a[:5]).shape == (5,)
        assert np.array_equal(fit_selected(a,b).named_steps['select'].get_support(), selector.get_support())
