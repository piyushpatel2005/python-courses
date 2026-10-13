from solution import *

def test_01_behavior():
    """Combine column-specific transforms"""
    for values in ([2., 4., 8., 10.], [20., 40., 60., 80.]):
        frame = pd.DataFrame({"size": values, "kind": ["a", "b", "a", "c"], "id": ["i1", "i2", "i3", "i4"]})
        router = route_columns(frame, "size", "kind")
        assert isinstance(router, ColumnTransformer), "Return the fitted column router."
        out = router.transform(frame)
        assert out.shape == (4, 4)
        assert np.allclose(out[:, 0], (np.array(values)-np.mean(values))/np.std(values)), "Scale only the numeric branch."
        assert np.allclose(out[:, 1:].sum(axis=1), 1)
        names = router.get_feature_names_out()
        assert not any("id" in name for name in names)
        shifted = pd.DataFrame({"size": [100.], "kind": ["new"], "id": ["q"]})
        assert np.array_equal(router.transform(shifted)[0, 1:], [0, 0, 0])

