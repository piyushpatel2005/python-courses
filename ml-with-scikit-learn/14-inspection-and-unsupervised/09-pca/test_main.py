from solution import *

def test_01_pca():
    """Fit PCA on training data and inspect explained_variance_ratio_ without labeling components as selected raw features."""
    for offset in [0,4]:
        a = np.array([[1,2,0],[2,4,1],[3,6,0],[4,8,2],[5,10,1]],dtype=float)+offset
        model = fit_projection(a)
        assert isinstance(model,PCA) and model.n_components == 2
        z = model.transform(a)
        assert z.shape == (5,2)
        assert model.inverse_transform(z).shape == a.shape
        expected=PCA(n_components=2,svd_solver='full').fit(a)
        assert np.allclose(model.mean_,a.mean(axis=0))
        assert np.allclose(model.explained_variance_ratio_,expected.explained_variance_ratio_)
        assert np.allclose(model.inverse_transform(z),expected.inverse_transform(expected.transform(a)),atol=1e-8)
