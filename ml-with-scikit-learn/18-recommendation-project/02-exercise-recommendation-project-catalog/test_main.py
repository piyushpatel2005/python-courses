from solution import *

def test_01_recommendation_project_catalog():
    """Freeze the file-backed catalog and chronological partitions."""
    catalog=make_catalog()
    assert isinstance(catalog,pd.DataFrame)
    r=split_interactions(catalog,INTERACTIONS.sample(frac=1,random_state=7))
    assert r is not None
    users=set(INTERACTIONS['user_id'])
    assert len(r['train'])==3*len(users) and len(r['test'])==len(users)
    assert len(r['validation'])==len(users) and r['omitted']==[]
    assert isinstance(r['train'],pd.DataFrame)
    assert (r['train']['event_at'] <= '2025-01-19').all()
    assert (r['validation']['event_at']=='2025-01-26').all()
    assert (r['test']['event_at']=='2025-02-02').all()
    assert set(r['train']['user_id'])==set(USERS['user_id'])
    changed=catalog.copy(deep=True)
    first=changed.iloc[0]['item_id']
    changed.loc[changed.index[0],'available_since']='2025-01-20'
    r2=split_interactions(changed,INTERACTIONS)
    affected=set(INTERACTIONS.loc[INTERACTIONS['item_id']==first,'user_id'])
    assert affected <= set(r2['omitted'])
    assert first not in set(r2['train']['item_id'])
    assert split_interactions(catalog,INTERACTIONS.iloc[:-1])['omitted']
