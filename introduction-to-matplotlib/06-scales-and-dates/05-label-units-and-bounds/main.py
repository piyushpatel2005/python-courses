import matplotlib.pyplot as plt

hours = [9, 10, 11, 12]
people = [3, 12, 18, 15]
fig, ax = plt.subplots()
ax.plot(hours, people, marker="o")
ax.set(xlabel="Hour of day", ylabel="Occupancy (people)")
ax.set_ylim(0, 20)
