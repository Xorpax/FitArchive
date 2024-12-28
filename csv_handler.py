import csv
import pandas as pd

fp = ".\example1.csv"

with open(fp) as example_csv:
    reader = csv.reader(example_csv)
    for row in reader:
        print(row)

print(pd.read_csv(fp))
