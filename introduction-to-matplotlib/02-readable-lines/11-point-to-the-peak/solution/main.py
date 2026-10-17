import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([8, 10, 12], [3, 5, 9], marker="o")
ax.annotate("Wind peak", xy=(12, 9), xytext=(10, 11), arrowprops={"arrowstyle": "->"})
plt.show()
