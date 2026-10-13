from solution import *

def test_01_stage():
    """Exercise: set an operational threshold"""
    from types import SimpleNamespace
    for y,scores in [([1,0],[0.3,0.1]),([1,1,0],[0.1,0.2,0.9]),([1,0],[0.9,0.8]),([1,1,0],[0.5,0.7,0.2])]:
        validation=pd.DataFrame({'basket_value_usd':scores,'item_count':1,'category':'decor','returned_30d':y})
        model=SimpleNamespace(classes_=np.array([0,1]),predict_proba=lambda X:np.column_stack([1-X.basket_value_usd,X.basket_value_usd]))
        got=choose_threshold(model,validation)
        assert got is not None, 'Return a validation-selected threshold.'
        rows=[(t,precision_score(y,np.array(scores)>=t,zero_division=0),recall_score(y,np.array(scores)>=t,zero_division=0)) for t in [0.3,0.5,0.7]]
        feasible=[r for r in rows if r[2]>=0.75]
        expected=max(feasible,key=lambda r:(r[1],r[0]))[0] if feasible else max(rows,key=lambda r:(r[2],r[1],-r[0]))[0]
        assert got==expected, 'Apply the boundary, constraint, and tie policy.'
    splits=make_splits(make_data()); model=tune_model(splits['train']).best_estimator_
    before=model.named_steps['logistic'].coef_.copy()
    t=choose_threshold(model,splits['validation'])
    assert np.array_equal(before,model.named_steps['logistic'].coef_), 'Do not refit during threshold selection.'
    splits['test']['returned_30d']=1-splits['test']['returned_30d']
    assert t==choose_threshold(model,splits['validation'])
