import pandas as pd
import matplotlib.pyplot as plt

def plot_route_means(frame):
    fig, ax = plt.subplots()
    return fig, ax

sample = pd.DataFrame({"route": ["A", "B", "A"], "minutes": [8, 12, 14]})
fig, ax = plot_route_means(sample)
