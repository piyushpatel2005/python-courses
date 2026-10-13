from solution import *

def test_01_behavior():
    """Exercise: fit a nonlinear SVM"""
    X = np.array([[-2., -2.], [-2., 2.], [2., -2.], [2., 2.], [-1.8, -2.], [-1.8, 2.], [1.8, -2.], [1.8, 2.]])
    y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
    q = np.array([[-1.9, -1.9], [-1.9, 1.9], [1.9, -1.9], [1.9, 1.9]])
    actual = np.array([0, 1, 1, 0])
    for candidates in ([(0.5, 0.1), (5., 1.)], [(2., 0.5), (8., 2.)]):
        got = select_rbf(X, y, q, actual, candidates)
        assert got is not None, "Return the RBF setting and validation scores."
        choice, scores = got
        expected = []
        for C, gamma in candidates:
            reference = Pipeline([("scale", StandardScaler()), ("model", SVC(kernel="rbf", C=C, gamma=gamma))]).fit(X, y)
            expected.append(reference.score(q, actual))
        assert np.allclose(scores, expected), "Fit and evaluate RBF, not a linear kernel."
        assert tuple(choice) == candidates[int(np.argmax(expected))]

