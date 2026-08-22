import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

# Line plot
plt.plot(df["sepal_length"])
plt.title("Sepal Length")
plt.xlabel("Index")
plt.ylabel("Length")
plt.show()

# Scatter plot
plt.scatter(df["sepal_length"], df["petal_length"])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

# Bar chart
df.groupby("species")["petal_length"].mean().plot(kind="bar")
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.show()

# Histogram
plt.hist(df["sepal_length"], bins=10)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# Pie chart
df["species"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Iris Species Distribution")
plt.ylabel("")
plt.show()

# Subplots
df[["sepal_length", "sepal_width", "petal_length", "petal_width"]].plot(
    subplots=True,
    layout=(2, 2),
    figsize=(10, 7)
)

plt.tight_layout()
plt.show()