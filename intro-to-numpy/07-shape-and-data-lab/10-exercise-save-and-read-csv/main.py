from io import StringIO
import numpy as np

def save_grid(grid):
    buffer = StringIO()
    # Write numeric grid into buffer with comma delimiter and fmt="%d".
    return buffer.getvalue()

def read_grid(text):
    # Read the CSV text back as a 2D array of integers.
    return np.empty((0, 0), dtype=int)

weather = np.array([[6, 9], [2, 4]])
text = save_grid(weather)
print("CSV:", repr(text))
print("loaded:", read_grid(text))
