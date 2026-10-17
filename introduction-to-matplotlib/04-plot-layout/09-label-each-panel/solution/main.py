import matplotlib.pyplot as plt

def label_panels(days, temperature, moisture):
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(days, temperature)
    axes[0].set_title("(a) Temperature")
    axes[0].set_ylabel("°C")
    axes[1].plot(days, moisture)
    axes[1].set_title("(b) Moisture")
    axes[1].set_ylabel("%")
    return fig, axes

fig, axes = label_panels([1, 2, 3], [19, 22, 20], [43, 38, 46])
