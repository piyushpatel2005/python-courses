from solution import *

def test_01_tfidf():
    """Fit TfidfVectorizer and calculate smoothed IDF then row normalization on a tiny example."""
    for docs,queries in [(['linen linen cover','cotton cover'],['linen cover','novelword']),(['glass bowl','wood bowl bowl','wood tray'],['bowl wood','tray'])]:
        result=encode_tfidf(docs,queries)
        assert result is not None
        v,z=result
        expected=TfidfVectorizer(max_features=100,smooth_idf=True,norm='l2').fit(docs)
        assert issparse(z) and v.vocabulary_ == expected.vocabulary_
        assert np.allclose(v.idf_,expected.idf_)
        assert np.allclose(z.toarray(),expected.transform(queries).toarray(),atol=1e-10)
        norms=np.sqrt(z.multiply(z).sum(axis=1)).A1
        assert np.all(np.isclose(norms,0)|np.isclose(norms,1))
