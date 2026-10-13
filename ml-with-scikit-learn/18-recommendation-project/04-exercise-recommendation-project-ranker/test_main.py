from solution import *

def test_01_recommendation_project_ranker():
    """Add a train-only TF-IDF profile scorer and deterministic filtered top-k function."""
    from scipy.sparse import csr_matrix
    ids=['Z','A','B','C']
    matrix=csr_matrix([[1,0],[1,0],[0,1],[1,0]])
    training=[('U','C','2025-01-05','view')]
    assert recommend(ids,matrix,training,'U',3)==['A','Z','B']
    assert recommend(ids,matrix,training,'new',3)==[]
    assert recommend(ids,0*matrix,training,'U',3)==[]
    assert recommend(ids,matrix,[('U','B','2025-01-05','view')],'U',2)==['A','C']
    assert recommend(ids,matrix,training,'U',1)==['A']
    order=[2,0,3,1]
    assert recommend([ids[i] for i in order],matrix[order],training,'U',3)==['A','Z','B']
    parts=split_interactions(make_catalog(),INTERACTIONS)
    item_ids,v,features=build_profiles(make_catalog())
    before=features.copy()
    recommend(item_ids,features,parts['train'],parts['train'].iloc[0]['user_id'],3)
    assert (features!=before).nnz==0
