from solution import *

def test_01_dbscan():
    """Fit DBSCAN with explicit eps and min_samples and identify noise without forcing every row into a cluster."""
    for shift in [0,5]:
        a=np.array([[0,0],[0.1,0],[0,0.1],[3,3],[3.1,3],[3,3.1],[8,0],[8.1,0]])+shift
        labels=density_labels(a)
        assert labels is not None and len(labels)==8
        assert np.all(np.array(labels)[6:]==-1), "A pair does not meet min_samples=3."
        assert labels[0] == labels[1] == labels[2] != -1
        assert labels[3] == labels[4] == labels[5] != -1
        assert labels[0] != labels[3]
