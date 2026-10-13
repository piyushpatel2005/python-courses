from solution import *

def test_01_recommendation_project_report():
    """Freeze validation choices and compare final ranking metrics with popularity baseline plus scope limits."""
    from scipy.sparse import csr_matrix
    ids=['A','B','C','D']
    matrix=csr_matrix([[1,0],[1,0],[0,1],[0,1]])
    training=[('U','A','2025-01-05','view'),('V','C','2025-01-05','view')]
    heldout=[('U','B','2025-02-02','view'),('V','A','2025-02-02','view')]
    r=evaluate(ids,matrix,training,heldout,3)
    assert r is not None and r['users']==2 and r['k']==3
    assert r['training_events']==2 and r['heldout_events']==2
    assert r['catalog_items']==4 and r['frozen_history'] is True
    assert np.isclose(r['content']['precision'],1/3)
    assert np.isclose(r['content']['recall'],1)
    assert np.isclose(r['content']['ndcg'],(1+1/np.log2(3))/2)
    assert np.isclose(r['popularity']['ndcg'],(1+1/np.log2(3))/2)
    assert r['content']['coverage']==1
    more=heldout+[('U','D','2025-02-02','view'),('cold','A','2025-02-02','view')]
    r2=evaluate(ids,matrix,training,more,1)
    assert r2['omitted']==['cold']
    assert np.isclose(r2['content']['precision'],0.5)
    assert np.isclose(r2['content']['recall'],0.25)
    assert np.isclose(r2['content']['hit'],0.5)
    assert training==[('U','A','2025-01-05','view'),('V','C','2025-01-05','view')]
    short=evaluate(['A','B'],csr_matrix([[1,0],[1,0]]),training[:1],heldout[:1],3)
    assert np.isclose(short['content']['precision'],1/3)
    assert evaluate(ids,matrix,training,[],3)['users']==0
