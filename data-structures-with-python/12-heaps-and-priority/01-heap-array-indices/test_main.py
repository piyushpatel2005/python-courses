from solution import *

def test_01_checkpoint():
    'In `family_indices`, reject an index outside the heap shape.'
    for i,n in ((-1,4),(4,4),(0,0),(0,-1)):
        try: family_indices(i,n)
        except IndexError: pass
        else: assert False

def test_02_checkpoint():
    'In `family_indices`, return the parent and existing child positions, using `None` for missing relatives.'
    assert family_indices(0,1)==(None,None,None)
    assert family_indices(0,6)==(None,1,2)
    assert family_indices(1,6)==(0,3,4)
    assert family_indices(2,6)==(0,5,None)
    assert family_indices(5,6)==(2,None,None)

