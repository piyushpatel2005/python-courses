import matplotlib.pyplot as plt

hours = [8, 10, 12]
fig, ax = plt.subplots()
ax.plot(hours, [14, 18, 22], label="Sun")
ax.plot(hours, [12, 15, 17], label="Second bed")
ax.legend()
plt.show()
