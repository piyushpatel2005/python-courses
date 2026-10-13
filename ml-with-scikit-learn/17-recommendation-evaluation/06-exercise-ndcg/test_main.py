from solution import *

def test_01_ndcg():
    """Compute binary relevance DCG and normalized DCG with an explicit zero-IDCG policy."""
    assert np.isclose(binary_ndcg(['X','A','Y'],{'A'},3),1/np.log2(3))
    assert np.isclose(binary_ndcg(['A','B'],{'A','B'},3),1)
    assert np.isclose(binary_ndcg(['A','A','X'],{'A','B'},3),1/(1+1/np.log2(3)))
    assert binary_ndcg(['A'],set(),3)==0
    assert binary_ndcg([],{'A'},3)==0
    assert binary_ndcg(['A','X'],{'A'},2)>binary_ndcg(['X','A'],{'A'},2)
