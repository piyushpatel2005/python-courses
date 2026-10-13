from solution import *

def test_01_cold_start():
    """Use training-only item popularity for no-history or zero-vector users and state coverage and bias limits."""
    events=pd.DataFrame([('U','B'),('V','B'),('V','C')],columns=['user_id','item_id'])
    assert popular_items(['D','A','C','B'],events,{'B'},3)==['C','A','D']
    assert popular_items(['C','B','A'],events.iloc[:0],set(),3)==['A','B','C']
    assert popular_items(['A'],events,{'A'},3)==[]
    assert popular_items(['C','B','A'],events,set(),1)==['B']
    assert popular_items(['C','B','A'],pd.DataFrame([('U','A')],columns=['user_id','item_id']),set(),2)==['A','B']
