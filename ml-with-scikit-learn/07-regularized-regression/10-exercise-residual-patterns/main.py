import numpy as np
import matplotlib.pyplot as plt


def residual_plot(actual, predicted):
    return None

predicted = np.array([15., 25., 35., 45., 55., 65.])
actual = np.array([21., 26., 31., 41., 56., 71.])

chart = residual_plot(actual, predicted)
print("Residuals:", actual-predicted)
print("Positive ends and a negative middle suggest missed curvature, not its cause.")
if chart is not None:
    plt.show()
