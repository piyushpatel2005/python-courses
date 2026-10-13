from solution import *
from sklearn.datasets import make_blobs

def test_01_kmeans():
    """Fit KMeans with explicit n_init=10 and seed and inspect centers without using target labels."""
    for seed in [3,9]:
        a,_=make_blobs(n_samples=36,centers=[[-4,0],[0,4],[4,0]],cluster_std=0.2,random_state=seed)
        model=fit_clusters(a)
        assert isinstance(model,KMeans) and model.n_clusters == 3
        assert model.n_init == 10 and model.random_state == 17
        distances=((a[:,None,:]-model.cluster_centers_[None,:,:])**2).sum(axis=2)
        assert np.array_equal(model.labels_,distances.argmin(axis=1))
        for label in range(3):
            assert np.allclose(model.cluster_centers_[label],a[model.labels_==label].mean(axis=0))
        assert np.isclose(model.inertia_,distances.min(axis=1).sum())
