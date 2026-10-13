from solution import *

def test_01_cluster_validation():
    """Compute silhouette_score only for valid cluster counts and explain its geometric assumptions."""
    a=np.array([[0,0],[0,1],[5,0],[5,1]],dtype=float)
    assert safe_silhouette(a,[0,0,0,0]) is None
    assert safe_silhouette(a,[0,1,2,3]) is None
    for labels in [[0,0,1,1],[7,7,2,2],[0,1,0,1]]:
        result=safe_silhouette(a,labels)
        assert result is not None and -1 <= result <= 1
        assert np.isclose(result,silhouette_score(a,labels),atol=1e-12)
