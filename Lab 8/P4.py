import pandas as pd

df = pd.read_csv("titanic.csv")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

df = df[df["Age"] >= 0]

df = df.drop_duplicates()

print("Cleaned Titanic Data:")
print(df.head())

print("\nData Information:")
df.info()