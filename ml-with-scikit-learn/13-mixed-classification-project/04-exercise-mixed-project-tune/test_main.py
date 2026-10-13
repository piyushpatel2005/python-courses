from solution import *

def test_01_stage():
    """Exercise: tune with stratified folds"""
    splits=make_splits(make_data()); train=splits['train']
    search=tune_model(train)
    assert search is not None, 'Return a search fitted only on its train argument.'
    assert search.param_grid=={'logistic__C':[0.1,1.,10.]}
    assert search.scoring=='f1_macro' and search.n_splits_==3 and search.refit is True and search.n_jobs==1
    branch=search.best_estimator_.named_steps['preprocess'].named_transformers_['numeric']
    assert np.allclose(branch.named_steps['impute'].statistics_,np.nanmedian(train[['basket_value_usd','item_count']],axis=0))
    assert branch.named_steps['scale'].n_samples_seen_==108
    changed=train.copy(); changed['basket_value_usd']+=1000
    changed_search=tune_model(changed)
    assert np.isclose(changed_search.best_estimator_.named_steps['preprocess'].named_transformers_['numeric'].named_steps['impute'].statistics_[0],branch.named_steps['impute'].statistics_[0]+1000)
    for tr,va in search.cv.split(train[FEATURES],train.returned_30d):
        assert not set(train.iloc[tr].order_id)&set(train.iloc[va].order_id)
        assert not set(train.iloc[tr].order_id)&set(splits['validation'].order_id)
