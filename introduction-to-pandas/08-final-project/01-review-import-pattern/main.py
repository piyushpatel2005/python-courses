from io import StringIO
import pandas as pd

def read_tickets(text):
    return pd.read_csv(StringIO(text), sep=";")

sample = "workshop,tickets\nPottery,7\nPrinting,4\n"
print(read_tickets(sample))
