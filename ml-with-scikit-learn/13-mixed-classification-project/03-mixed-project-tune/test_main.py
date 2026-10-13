from solution import *

def test_01_analogue():
    """Tune with stratified folds"""
    search=tune_model(make_analogue())
    assert search.scoring=='f1_macro', 'Select by macro F1, not accuracy.'
    assert search.param_grid=={'logistic__C':[0.2,2.0]}
    assert search.n_splits_==3 and search.n_jobs==1
