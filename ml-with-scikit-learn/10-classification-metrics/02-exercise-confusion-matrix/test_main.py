from solution import *

def test_01_behavior():
    """Exercise: count classification outcomes"""
    for y, pred, labels in [([0,0,0,1,1],[0,1,1,0,1],[0,1]), (['yes','no','yes'],['yes','yes','yes'],['no','yes'])]:
        result = summarize(y, pred, labels)
        assert result is not None, 'Return the matrix and accuracy.'
        matrix, score = result
        expected = np.array([[sum(a == i and b == j for a,b in zip(y,pred)) for j in labels] for i in labels])
        assert np.array_equal(matrix, expected), 'Rows must be actual labels in supplied order.'
        assert np.isclose(score, np.mean(np.array(y)==np.array(pred)))
