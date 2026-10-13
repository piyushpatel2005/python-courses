from solution import *

def test_01_recommendation_project_fallback():
    """Extend the project function with training-popularity fallback for no-history and zero-vector inputs."""
    from scipy.sparse import csr_matrix
    ids=['D','B','A','C']
    matrix=csr_matrix([[0,1],[1,0],[1,0],[0,1]])
    training=[('U','B','2025-01-05','view'),('V','C','2025-01-05','view'),('W','C','2025-01-05','view')]
    assert recommend_with_fallback(ids,matrix,training,'new',3)==['C','B','A']
    assert recommend_with_fallback(ids,matrix,training,'U',3)==recommend(ids,matrix,training,'U',3)
    assert recommend_with_fallback(ids,0*matrix,training,'U',3)==['C','A','D']
    assert recommend_with_fallback(ids,matrix,[],'new',2)==['A','B']
    assert recommend_with_fallback(['A'],csr_matrix([[0,0]]),[('U','A','2025-01-05','view')],'U',3)==[]
