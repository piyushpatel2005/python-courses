import matplotlib.pyplot as plt

def shift_colors(days, morning, afternoon):
    fig, ax = plt.subplots()
    ax.plot(days, morning, label="Morning", color="tab:blue")
    ax.plot(days, afternoon, label="Afternoon", color="tab:orange")
    ax.legend()
    return fig

fig = shift_colors([1, 2, 3], [16, 20, 19], [13, 22, 23])
plt.show()
