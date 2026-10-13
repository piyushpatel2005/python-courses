import numpy as np
import matplotlib.pyplot as plt


def residual_plot(actual, predicted):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.scatter(predicted, predicted-actual)
    ax.axhline(0, color="gray", linewidth=1)
    ax.set_xlabel("Predicted price (USD)")
    ax.set_ylabel("Observed - predicted (USD)")
    fig.tight_layout()
    return fig, ax

predicted = np.array([10., 20., 30., 40., 50.])
actual = np.array([14., 19., 27., 39., 54.])

chart = residual_plot(actual, predicted)
print("Residuals:", actual-predicted)
print("Positive ends and a negative middle suggest missed curvature, not its cause.")
if chart is not None:
    plt.show()
