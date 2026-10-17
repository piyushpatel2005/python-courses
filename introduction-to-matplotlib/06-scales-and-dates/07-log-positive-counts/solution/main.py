import matplotlib.pyplot as plt

weeks = [1, 2, 3, 4]
attendees = [1, 10, 100, 1000]
fig, ax = plt.subplots()
ax.plot(weeks, attendees, marker="o")
ax.set_yscale("log")
ax.set_ylim(1, 1000)
ax.set(xlabel="Week", ylabel="Attendees (people)")
