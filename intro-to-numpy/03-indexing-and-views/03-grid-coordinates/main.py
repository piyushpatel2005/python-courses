import numpy as np
grid = np.array([[8, 3, 5], [4, 7, 9]])
spot = grid[0, 1]  # Change the row to 1.
print(spot)
print(grid[:, 1])  # The entire middle column, across both rows.
