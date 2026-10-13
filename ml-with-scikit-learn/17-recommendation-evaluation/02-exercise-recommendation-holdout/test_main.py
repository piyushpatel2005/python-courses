from solution import *

def test_01_recommendation_holdout():
    """Create per-user chronological validation/test interactions and define the available candidate catalog at cutoff."""
    events=[('A',str(i),f'2025-01-{i:02d}') for i in range(1,6)]
    events += [('B','1','2025-01-01'),('A','future','2025-02-01')]
    events=pd.DataFrame(events,columns=['user_id','item_id','event_at'])
    r=chronological_holdout(events.iloc[::-1],set('12345'))
    assert r is not None and r['omitted']==['B']
    assert [e[1] for e in r['train']]==['1','2','3']
    assert r['validation']==[('A','4','2025-01-04')]
    assert r['test']==[('A','5','2025-01-05')]
    assert chronological_holdout(events,set('12'))['train']==[]
    assert not set(r['train']) & set(r['test'])
