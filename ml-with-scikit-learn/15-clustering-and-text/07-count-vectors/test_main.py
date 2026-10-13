from solution import *

def test_01_count_vectors():
    """Fit CountVectorizer on training text and inspect vocabulary sparse shape and a tiny dense slice."""
    for docs,queries in [(['linen linen cover','cotton cover'],['linen','unseenword']), (['glass bowl','wood bowl bowl'],['bowl bowl','glass'])]:
        result=encode_counts(docs,queries)
        assert result is not None
        vectorizer,matrix=result
        expected=CountVectorizer(max_features=100).fit(docs)
        assert issparse(matrix)
        assert vectorizer.vocabulary_ == expected.vocabulary_, "Fit vocabulary on training text only."
        assert np.array_equal(matrix.toarray(),expected.transform(queries).toarray())
        assert np.array_equal(encode_counts(docs,list(reversed(queries)))[1].toarray(),matrix.toarray()[::-1])
