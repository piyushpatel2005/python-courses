from io import StringIO
import numpy as np

csv_text = "3,8\n5,2\n"  # Two sensor rows.
readings = np.genfromtxt(StringIO(csv_text), delimiter=";", dtype=int)
print("shape:", readings.shape)
print(readings)
