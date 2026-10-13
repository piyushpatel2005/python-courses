from solution import *

def test_01_stage():
    """Exercise: assemble a mixed-feature classifier"""
    data=make_data(); splits=make_splits(data)
    assert len(data)==180 and data.order_id.is_unique and data.customer_id.is_unique
    assert [len(splits[k]) for k in ['train','validation','test']]==[108,36,36]
    ids=[set(splits[k].order_id) for k in ['train','validation','test']]
    assert not ids[0]&ids[1] and not ids[0]&ids[2] and not ids[1]&ids[2]
    assert set.union(*ids)==set(data.order_id)
    for delta in [0,500]:
        train=splits['train'].copy(); train['basket_value_usd']+=delta
        model=build_model()
        assert model is not None, 'Return an unfitted mixed pipeline.'
        model.fit(train[FEATURES],train.returned_30d)
        branch=model.named_steps['preprocess'].named_transformers_['numeric']
        assert np.allclose(branch.named_steps['impute'].statistics_,np.nanmedian(train[['basket_value_usd','item_count']],axis=0))
        query=pd.DataFrame({'basket_value_usd':[np.nan,30.], 'item_count':[2.,np.nan], 'category':['decor','kitchen']})
        assert np.isfinite(model.predict_proba(query)).all()
        assert set(model.feature_names_in_)==set(FEATURES)
        leaked=train.copy(); leaked['actual_delivery_days']=10000; leaked['order_id']='changed'
        assert np.allclose(model.predict_proba(train),model.predict_proba(leaked))
