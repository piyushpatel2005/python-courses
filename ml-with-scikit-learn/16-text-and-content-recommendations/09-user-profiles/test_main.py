from solution import *

def test_01_user_profiles():
    """Build a mean profile from training interactions only and rank unseen items."""
    a=csr_matrix([[1,0],[0,2],[3,1]])
    assert np.allclose(mean_profile(['A','B','C'],a,['A','B']),[[0.5,1]])
    assert np.allclose(mean_profile(['A','B','C'],a,['B','B','C']),[[1.5,1.5]])
    assert np.array_equal(mean_profile(['A','B','C'],a,[]),np.zeros((1,2)))
    assert np.allclose(mean_profile(['A','B','C'],a,['missing','C']),[[3,1]])
    assert np.allclose(mean_profile(['C','A','B'],a[[2,0,1]],['A','B']),[[0.5,1]])
