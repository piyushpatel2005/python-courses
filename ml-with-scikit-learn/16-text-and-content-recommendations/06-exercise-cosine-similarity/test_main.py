from solution import *

def test_01_cosine_similarity():
    """Compute cosine_similarity and handle zero-vector similarity explicitly."""
    a=csr_matrix([[3,0],[0,2],[1,1],[0,0]])
    z=compare_vectors(a,a)
    assert z is not None and z.shape==(4,4)
    assert np.allclose(z,z.T)
    assert np.allclose(np.diag(z)[:3],1)
    assert np.allclose(z[3],0)
    assert np.isclose(z[0,2],1/np.sqrt(2))
    assert np.allclose(compare_vectors(2*a[:2],a),z[:2])
