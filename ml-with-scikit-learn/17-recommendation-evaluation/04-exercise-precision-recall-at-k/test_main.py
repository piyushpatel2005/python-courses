from solution import *

def test_01_precision_recall_at_k():
    """Compute precision@k and recall@k using a declared denominator policy and macro averaging over eligible users."""
    assert topk_metrics(['A'],{'A','B'},3)=={'precision':1/3,'recall':0.5,'hit':1.0}
    assert topk_metrics(['A','A','B'],{'A','B'},3)=={'precision':2/3,'recall':1.0,'hit':1.0}
    assert topk_metrics(['X','Y','A'],{'A'},2)=={'precision':0.0,'recall':0.0,'hit':0.0}
    assert topk_metrics([],{'A'},3)=={'precision':0.0,'recall':0.0,'hit':0.0}
    assert topk_metrics(['A'],set(),3) is None
