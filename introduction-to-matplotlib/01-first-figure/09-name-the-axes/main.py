import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([8, 10, 12], [41, 48, 52])
ax.set_xlabel("Hour")
ax.set_ylabel("Reading")
plt.show()
