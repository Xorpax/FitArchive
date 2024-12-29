import pandas as pd

fp = r".\example1.csv"

data = pd.read_csv(fp)
# df = data.to_series
print(data)
