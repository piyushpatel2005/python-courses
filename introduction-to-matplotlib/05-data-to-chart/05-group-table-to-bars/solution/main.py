import pandas as pd
import matplotlib.pyplot as plt

observations = pd.DataFrame({"park": ["Oak", "Pine", "Oak", "Pine"], "visitors": [10, 30, 20, 40]})
means = observations.groupby("park")["visitors"].mean()
fig, ax = plt.subplots()
ax.bar(means.index, means.to_numpy())
ax.set(title="Mean visitors by park", xlabel="Park", ylabel="Mean visitors (people)")
