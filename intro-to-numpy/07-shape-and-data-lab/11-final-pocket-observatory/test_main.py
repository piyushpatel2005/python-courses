from solution import *

def test_01_shape_sky():
    for strip in (np.arange(6) + 3, np.arange(12) + 1):
        grid = make_sky_grid(strip)
        assert grid.shape == (strip.size // 3, 3) and np.array_equal(grid.ravel(), strip)

def test_02_schedule_exposures():
    for settings in (np.array([2, 5]), np.array([1, 4, 8])):
        result = exposure_schedule(settings)
        expected = np.tile(np.repeat(settings[:, np.newaxis], 2, axis=0), (1, 2))
        assert np.array_equal(result, expected) and result.shape == (settings.size * 2, 2)

def test_03_export_sky():
    for grid in (np.array([[3, 6, 9], [2, 5, 8]]), np.array([[7, 1, 4]])):
        text = export_sky(grid)
        assert text.endswith("\n")
        assert [list(map(int, row.split(","))) for row in text.strip().splitlines()] == grid.tolist()

def test_04_import_sky():
    for text, expected in (("3,6,9\n2,5,8\n", [[3, 6, 9], [2, 5, 8]]), ("7,1,4\n", [[7, 1, 4]])):
        result = import_sky(text)
        assert result.dtype.kind in "iu" and np.array_equal(result, expected)
        assert result.shape == np.array(expected).shape

def test_05_observation_report():
    for grid, expected in ((np.array([[3, 6, 9], [2, 5, 8]]), "Rows: 2; brightest: 9; row means: 6.0, 5.0"), (np.array([[1, 2, 3]]), "Rows: 1; brightest: 3; row means: 2.0")):
        assert observation_report(grid) == expected
