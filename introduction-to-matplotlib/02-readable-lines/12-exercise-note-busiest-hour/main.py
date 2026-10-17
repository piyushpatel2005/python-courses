import matplotlib.pyplot as plt

def busiest_hour(hours, counts):
    fig, ax = plt.subplots()
    ax.plot(hours, counts, marker="o")
    # Use the first maximum; do not fix the peak to the sample hour.
    return fig

fig = busiest_hour([9, 11, 14], [12, 19, 16])
plt.show()
