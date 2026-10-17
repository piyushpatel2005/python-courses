import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 7, 6], label="North gauge", color="tab:blue")
ax.plot([1, 2, 3], [3, 6, 5], label="South gauge", color="tab:orange")
ax.legend()
plt.show()
