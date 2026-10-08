import pandas as pd

def make_guest_csv(frame):
    return frame.to_csv(index=True)

sample = pd.DataFrame({"guest": ["Jo", "Kim"], "tickets": [2, 1]})
print(make_guest_csv(sample))
