from solution import scores
import numpy as np


def test_last_score():
    """Change only the final score to 12"""
    assert isinstance(scores, np.ndarray), "Keep scores as a NumPy array created with np.array(...)."
    assert scores.tolist() == [4, 6, 12], "Keep 4 and 6, then change the last score to 12."
