# ==========================================
# Python Libraries Assignment
# Data Analysis & Visualization with Pandas and Matplotlib
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------

# Load Iris dataset from sklearn and convert to a DataFrame
iris = load_iris()
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first few rows
print("\n--- First 5 Rows ---")
print(df.head())

# Inspect structure
print("\n--- Data Info ---")
print(df.info())

# Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Clean data (fill missing values if any – here we don't have missing data)
# Example of handling missing values:
# df.fillna(df.mean(), inplace=True)

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

print("\n--- Statistical Summary ---")
print(df.describe())

# Grouping: Average petal length per species
grouped = df.groupby("species")["petal length (cm)"].mean()
print("\n--- Average Petal Length by Species ---")
print(grouped)

# Observations
print("\n--- Observations ---")
print("• Iris-virginica has the highest average petal length.")
print("• Iris-setosa generally has the smallest measurements across features.")

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# 1️⃣ Line Chart – Trend of sepal length across the dataset index
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], color="green", marker="o", linestyle="--", markersize=4)
plt.title("Sepal Length Trend Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2️⃣ Bar Chart – Average petal length per species
plt.figure(figsize=(6,4))
grouped.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# 3️⃣ Histogram – Distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=15, color="blue", edgecolor="black")
plt.title("Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4️⃣ Scatter Plot – Sepal length vs Petal length
plt.figure(figsize=(6,4))
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], color="red", alpha=0.7)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

print("\nAnalysis Complete ✅")
