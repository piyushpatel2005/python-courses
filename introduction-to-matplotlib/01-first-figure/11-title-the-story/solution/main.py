import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [26, 29, 27])
ax.set_xlabel("Day")
ax.set_ylabel("Moisture (%)")
ax.set_title("Garden soil moisture")
plt.show()
