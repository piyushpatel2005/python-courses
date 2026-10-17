import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [5, 7, 4], label="Observed", linestyle="-")
ax.plot([1, 2, 3], [6, 6, 6], label="Planned", linestyle="--")
ax.legend()
plt.show()
