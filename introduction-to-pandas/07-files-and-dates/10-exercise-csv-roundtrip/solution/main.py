from io import StringIO
import pandas as pd

def roundtrip_table(frame):
    text = frame.to_csv(index=False)
    restored = pd.read_csv(StringIO(text))
    return text, restored

sample = pd.DataFrame({"product": ["Tea", "Bread"], "units": [2, 5]})
text, restored = roundtrip_table(sample)
print(text)
print(restored)
