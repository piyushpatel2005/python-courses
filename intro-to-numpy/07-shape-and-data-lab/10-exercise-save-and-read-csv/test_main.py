from solution import *

def test_01_export_csv():
    for grid in (np.array([[6, 9], [2, 4]]), np.array([[11, 7, 3]])):
        text = save_grid(grid)
        assert text.endswith("\n")
        lines = text.strip().splitlines()
        assert len(lines) == grid.shape[0]
        assert [list(map(int, line.split(","))) for line in lines] == grid.tolist()

def test_02_import_csv():
    for text, expected in (("6,9\n2,4\n", [[6, 9], [2, 4]]), ("11,7,3\n", [[11, 7, 3]])):
        result = read_grid(text)
        assert result.dtype.kind in "iu" and result.shape == np.array(expected).shape
        assert np.array_equal(result, expected)
