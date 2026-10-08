from solution import *

def test_01():
    """Stack deliveries and reset the index."""
    a=pd.DataFrame({"product":["Rice"],"units":[3]},index=[20])
    b=pd.DataFrame({"product":["Oil","Salt"],"units":[2,5]},index=[30,31])
    pd.testing.assert_frame_equal(stack_deliveries(a,b),pd.concat([a,b],ignore_index=True))

def test_02():
    """Attach prices while rejecting duplicates."""
    a=pd.DataFrame({"product":["Rice","Oil","Rice"],"units":[3,2,1]})
    b=pd.DataFrame({"product":["Rice"],"price":[6]})
    pd.testing.assert_frame_equal(add_prices(a,b),a.merge(b,on="product",how="left",validate="many_to_one"))
    try:
        add_prices(a,pd.DataFrame({"product":["Rice","Rice"],"price":[6,7]}))
    except pd.errors.MergeError:
        pass
    else:
        assert False,"Reject duplicate price keys."

def test_03():
    """Count missing prices."""
    ledger=pd.DataFrame({"product":["X","Y","Z","W"],"price":[2,None,None,9]})
    assert unpriced_count(ledger)==2,"Count missing price cells."
    assert unpriced_count(ledger.iloc[[0,3]])==0,"A fully priced ledger has no gaps."
