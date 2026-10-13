from solution import *

def test_01_item_profiles():
    """Create one text profile per item with stable item IDs and disclose content-based rather than collaborative scope."""
    rows=[{'item_id':'Z9','category':'kitchen','title':'steel pan','description':'metal cook','outcome':'secretlabel'},
          {'item_id':'A1','category':'kitchen','title':'wood bowl','description':'wood serve','outcome':'futurelabel'}]
    rows=pd.DataFrame(rows)
    result=item_profiles(rows)
    assert result is not None
    ids,v,z=result
    assert ids == ['A1','Z9'] and issparse(z)
    texts=['kitchen wood bowl wood serve','kitchen steel pan metal cook']
    assert np.allclose(z.toarray(),v.transform(texts).toarray())
    assert not {'secretlabel','futurelabel','z9','a1'} & set(v.vocabulary_)
    ids2,v2,z2=item_profiles(rows.iloc[::-1])
    assert ids2==ids and np.allclose(z.toarray(),z2.toarray())
