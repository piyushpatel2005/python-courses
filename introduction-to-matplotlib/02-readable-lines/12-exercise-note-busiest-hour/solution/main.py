import matplotlib.pyplot as plt

def busiest_hour(hours, counts):
    fig, ax = plt.subplots()
    ax.plot(hours, counts, marker="o")
    peak_index = list(counts).index(max(counts))
    peak_hour = hours[peak_index]
    peak_count = counts[peak_index]
    ax.annotate(f"Peak: {peak_count}", xy=(peak_hour, peak_count),
                xytext=(peak_hour, peak_count + 3), arrowprops={"arrowstyle": "->"})
    return fig

fig = busiest_hour([9, 11, 14], [12, 19, 16])
plt.show()
