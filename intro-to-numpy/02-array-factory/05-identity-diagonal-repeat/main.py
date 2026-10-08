import numpy as np
# Sound board: grow the identity cue to four channels.
cue = np.eye(3)
gains = np.diag([2, 5, 7])
echo = np.repeat([4], 3)
print(cue.shape, gains.diagonal().tolist(), echo.tolist())
