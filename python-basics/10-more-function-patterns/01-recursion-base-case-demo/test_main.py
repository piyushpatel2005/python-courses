from solution import step_down, sample

def test_sample_countdown():
    assert sample == [3, 2, 1, 0]
    assert step_down(0) == [0]
