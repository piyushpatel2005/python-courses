from solution import *

def test_01():
    """Build a zero-filled grid with repeated cells summed."""
    a=pd.DataFrame({"zone":["E","W","E","E"],"day":["Mon","Tue","Tue","Mon"],"amount":[5.0,9.0,3.0,4.0]})
    pd.testing.assert_frame_equal(revenue_grid(a),pd.pivot_table(a,index="zone",columns="day",values="amount",aggfunc="sum",fill_value=0))

def test_02():
    """Report revenue and entries by zone."""
    a=pd.DataFrame({"zone":["E","E","W"],"day":["Mon","Tue","Mon"],"amount":[5.0,None,9.0]})
    pd.testing.assert_frame_equal(zone_report(a),a.groupby("zone").agg(revenue=("amount","sum"),entries=("amount","size")))

def test_03():
    """Count missing amounts independently of the pivot."""
    a=pd.DataFrame({"zone":["E","W","E"],"day":["M","M","T"],"amount":[None,7.0,None]})
    assert missing_amounts(a)==2,"Count missing amount cells."
    assert missing_amounts(a.iloc[[1]])==0,"A complete row has no gaps."
