import pandas as pd

df = pd.read_csv("sami.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nData Information:")
df.info()