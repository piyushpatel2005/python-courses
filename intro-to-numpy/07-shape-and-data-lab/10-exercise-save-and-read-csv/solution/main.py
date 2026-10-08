from io import StringIO
import numpy as np

def save_grid(grid):
    buffer = StringIO()
    np.savetxt(buffer, grid, delimiter=",", fmt="%d")
    return buffer.getvalue()

def read_grid(text):
    return np.genfromtxt(StringIO(text), delimiter=",", dtype=int, ndmin=2)

weather = np.array([[6, 9], [2, 4]])
text = save_grid(weather)
print("CSV:", repr(text))
print("loaded:", read_grid(text))
