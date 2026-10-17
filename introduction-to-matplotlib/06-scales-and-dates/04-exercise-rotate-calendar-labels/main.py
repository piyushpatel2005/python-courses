import pandas as pd
import matplotlib.pyplot as plt

def plot_collection_dates(frame):
    fig, ax = plt.subplots()
    return fig, ax

sample = pd.DataFrame({"day": ["2024-05-01", "2024-05-04"], "bags": [7, 11]})
fig, ax = plot_collection_dates(sample)
