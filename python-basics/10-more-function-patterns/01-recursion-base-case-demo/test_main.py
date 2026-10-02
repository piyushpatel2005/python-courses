from solution import pulse_steps, sample

def test_sample_pulses():
    """The tower pulses down to zero"""
    assert sample == [3, 2, 1, 0]
    assert pulse_steps(0) == [0]
