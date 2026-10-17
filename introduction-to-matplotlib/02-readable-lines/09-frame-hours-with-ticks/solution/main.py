import matplotlib.pyplot as plt

hours = [8, 10, 12]
fig, ax = plt.subplots()
ax.plot(hours, [13, 18, 21])
ax.set_xticks(hours)
ax.set_xlim(7, 14)
plt.show()
