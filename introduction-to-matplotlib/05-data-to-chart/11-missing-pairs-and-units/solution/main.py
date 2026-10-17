import pandas as pd
import matplotlib.pyplot as plt

survey = pd.DataFrame({"temperature": [16, None, 22, 25], "walkers": [42, 38, None, 61]})
complete = survey.dropna(subset=["temperature", "walkers"])
fig, ax = plt.subplots()
ax.scatter(complete["temperature"], complete["walkers"])
ax.set(xlabel="Temperature (°C)", ylabel="Walkers (people)")
