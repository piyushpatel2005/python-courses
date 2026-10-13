from solution import *

def test_01_stage():
    """Exercise: report final classification errors"""
    from types import SimpleNamespace
    for threshold in [0.3,0.7]:
        test=pd.DataFrame({'basket_value_usd':[0.1,0.3,0.7,0.9], 'item_count':[1,2,3,4], 'category':['decor','kitchen','kitchen','bedding'], 'returned_30d':[0,1,0,1]})
        model=SimpleNamespace(classes_=np.array([0,1]),named_steps={'logistic':SimpleNamespace(C=1.0)},predict_proba=lambda X:np.column_stack([1-X.basket_value_usd,X.basket_value_usd]))
        result=final_report(model,threshold,test)
        assert result is not None, 'Return the frozen-model test audit.'
        expected=test.basket_value_usd.to_numpy()>=threshold
        assert np.array_equal(result['confusion_matrix'],confusion_matrix(test.returned_30d,expected,labels=[0,1]))
        assert np.isclose(result['precision'],precision_score(test.returned_30d,expected,zero_division=0))
        assert np.isclose(result['recall'],recall_score(test.returned_30d,expected,zero_division=0))
        assert result['n_test']==4 and result['positive_count']==2 and result['threshold']==threshold and result['selected_C']==1.
        assert result['category_counts']=={'kitchen':2,'decor':1,'bedding':1}
        assert 'synthetic' in result['limitations'].lower()
    splits=make_splits(make_data()); model=tune_model(splits['train']).best_estimator_
    threshold=choose_threshold(model,splits['validation'])
    before=model.named_steps['logistic'].coef_.copy()
    final_report(model,threshold,splits['test'])
    assert np.array_equal(before,model.named_steps['logistic'].coef_)
