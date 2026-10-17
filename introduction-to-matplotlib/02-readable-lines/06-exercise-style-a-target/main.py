import matplotlib.pyplot as plt

def attendance_target(days, actual, target):
    fig, ax = plt.subplots()
    ax.plot(days, actual, label="Actual", linestyle="-")
    ax.plot(days, target, label="Target", linestyle="-")
    ax.legend()
    return fig

fig = attendance_target([1, 2, 3], [18, 21, 16], [20, 20, 20])
plt.show()
