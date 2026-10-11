from io import StringIO
import pandas as pd

def roundtrip_table(frame):
    # Export without the index, then read the resulting string.
    return "", pd.DataFrame()

sample = pd.DataFrame({"product": ["Tea", "Bread"], "units": [2, 5]})
text, restored = roundtrip_table(sample)
print(text)
print(restored)
