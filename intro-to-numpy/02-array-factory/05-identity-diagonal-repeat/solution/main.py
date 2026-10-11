import numpy as np
cue = np.eye(4)
gains = np.diag([2, 5, 7])
echo = np.repeat([4], 3)
print(cue.shape, gains.diagonal().tolist(), echo.tolist())
