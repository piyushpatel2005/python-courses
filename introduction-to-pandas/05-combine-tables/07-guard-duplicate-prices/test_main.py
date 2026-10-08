from solution import *

def test_01():
    """Change validate from many_to_many to many_to_one."""
    a=pd.DataFrame({"product":["Tea","Tea","Cake"],"units":[1,3,2]})
    b=pd.DataFrame({"product":["Cake","Tea"],"price":[8,5]})
    actual = price_orders(a, b)
    expected = a.merge(b,on="product",how="left",validate="many_to_one")
    if isinstance(expected,tuple):
        assert len(actual)==len(expected), "Return every requested result."
        for got,want in zip(actual,expected):
            pd.testing.assert_series_equal(got,want)
    elif isinstance(expected,pd.DataFrame):
        pd.testing.assert_frame_equal(actual,expected)
    elif isinstance(expected,pd.Series):
        pd.testing.assert_series_equal(actual,expected)
    else:
        assert actual == expected, "Check the result with different input values."
    try:
        price_orders(a,pd.DataFrame({"product":["Tea","Tea"],"price":[5,6]}))
    except pd.errors.MergeError:
        pass
    else:
        assert False, "Reject duplicate product keys in the price table."
