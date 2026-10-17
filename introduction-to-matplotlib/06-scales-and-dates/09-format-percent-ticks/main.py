import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

months = [1, 2, 3]
share = [0.20, 0.35, 0.50]
fig, ax = plt.subplots()
ax.plot(months, share, marker="o")
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=1))
ax.set(xlabel="Month", ylabel="Recycled share")
