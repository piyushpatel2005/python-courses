from solution import *

def test_01_behavior():
    """Exercise: read linear regression coefficients"""
    for offset in (7., -11.):
        X = np.array([[0., 0.], [1., 0.], [0., 1.], [2., 3.]])
        model = LinearRegression(n_jobs=1).fit(X, offset + X @ np.array([2., -3.]))
        q = np.array([[5., 2.], [-1., 4.], [0., 0.]])
        got = reconstruct(model, q)
        assert got is not None, "Return the coefficient reconstruction."
        assert np.allclose(got, model.predict(q), atol=1e-8), "Include intercept and preserve feature order."
    import ast, solution
    source = ast.parse(open(solution.__file__).read())
    helper = next(n for n in source.body if isinstance(n, ast.FunctionDef) and n.name == "reconstruct")
    assert not any(isinstance(n, ast.Attribute) and n.attr == "predict" for n in ast.walk(helper)), "Reconstruct from the attributes rather than delegating to predict."

