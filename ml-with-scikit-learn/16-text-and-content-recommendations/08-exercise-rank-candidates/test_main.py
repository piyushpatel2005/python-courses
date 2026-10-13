from solution import *

def test_01_rank_candidates():
    """Exclude the query item and seen items and sort scores with stable ID tie breaking."""
    assert rank_items(['Z','A','Q','S'],[0.5,0.5,1,0.9],{'S'},'Q',3)==['A','Z']
    assert rank_items(['A','Z','S','Q'],[0.5,0.5,0.9,1],{'S'},'Q',1)==['A']
    assert rank_items(['A'],[1],{'A'},'Q',3)==[]
    assert rank_items(['A','B','C'],[0.1,0.7,0.4],set(),'X',2)==['B','C']
