import pandas as pd

df = pd.read_csv("Heart_disease_cleveland_new.csv")

print("Dataset shape:", df.shape)

print("\nFirst five rows:")
print(df.head())

columns = ["age", "chol", "trestbps", "thalach"]
data = df[columns]

print("\nSelected columns:")
print(data.head())
import matplotlib.pyplot as plt

columns = ["age", "chol", "trestbps", "thalach"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for ax, col in zip(axes.flatten(), columns):
    ax.hist(df[col], bins=20, edgecolor="black")
    ax.set_title(col)
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("histograms.png")
#plt.show()
from scipy.stats import shapiro

print("\nNormality Test (Shapiro-Wilk):")

for col in columns:
    stat, p = shapiro(df[col].dropna())

    print(f"\n{col}:")
    print(f"Statistic = {stat:.4f}")
    print(f"P-value = {p:.4f}")

    if p > 0.05:
        print("Approximately normal")
    else:
        print("Not normally distributed")
from scipy.stats import mannwhitneyu

healthy = df[df["target"] == 0]["thalach"]
disease = df[df["target"] == 1]["thalach"]

print("\nSession 2 - Heart Rate Comparison")

print("Healthy mean:", healthy.mean())
print("Disease mean:", disease.mean())

stat, p = mannwhitneyu(
    healthy,
    disease,
    alternative="two-sided"
)

print("Mann-Whitney U statistic:", stat)
print("P-value:", p)

if p < 0.05:
    print("Statistically significant difference")
else:
    print("No statistically significant difference")
import numpy as np

healthy_sem = healthy.sem()
disease_sem = disease.sem()

print("\nMean and Standard Error:")
print(f"Healthy: {healthy.mean():.2f} ± {healthy_sem:.2f}")
print(f"Disease: {disease.mean():.2f} ± {disease_sem:.2f}")

groups = ["Healthy", "Heart Disease"]
means = [healthy.mean(), disease.mean()]
errors = [healthy_sem, disease_sem]

plt.figure(figsize=(7, 5))

plt.bar(groups, means, yerr=errors, capsize=8)

plt.ylabel("Maximum Heart Rate (bpm)")
plt.title("Mean Maximum Heart Rate with SEM")

plt.savefig("heart_rate_comparison.png")
plt.close()
from scipy.stats import spearmanr

# Calculate correlation
r, p = spearmanr(df["age"], df["thalach"])

print("\nTask 5 - Age and Heart Rate Correlation")
print(f"Spearman correlation: {r:.4f}")
print(f"P-value: {p:.4f}")

# Create scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(df["age"], df["thalach"], alpha=0.6)

plt.xlabel("Age")
plt.ylabel("Maximum Heart Rate (bpm)")
plt.title("Age vs Maximum Heart Rate")

plt.savefig("age_thalach.png")
plt.close()
# Task 6 - Chemical Exposure Analysis

chem = pd.read_csv("chemicals_cancer.csv")

print("\nTask 6 - Chemical Dataset")

print("Dataset shape:")
print(chem.shape)

print("\nFirst five rows:")
print(chem.head())

print("\nColumn names:")
print(chem.columns.tolist())
# Task 6 - Naive Correlation Analysis

from scipy.stats import spearmanr

benzene_r, benzene_p = spearmanr(
    chem["benzene"], chem["malignancy"]
)

cadmium_r, cadmium_p = spearmanr(
    chem["cadmium"], chem["malignancy"]
)

print("\nTask 6 - Chemical Correlations")

print(f"Benzene correlation: {benzene_r:.4f}")
print(f"Benzene p-value: {benzene_p:.6f}")

print(f"Cadmium correlation: {cadmium_r:.4f}")
print(f"Cadmium p-value: {cadmium_p:.6f}")
# Task 7 - Controlling for Pollution
  
filtered = chem[
    (chem["pollution_index"] > 40) &
    (chem["pollution_index"] < 60)
]

print("\nTask 7 - Controlling for Pollution")
print("Number of patients:", len(filtered))

benzene_r, benzene_p = spearmanr(
    filtered["benzene"],
    filtered["malignancy"]
)

cadmium_r, cadmium_p = spearmanr(
    filtered["cadmium"],
    filtered["malignancy"]
)

print(f"Benzene correlation: {benzene_r:.4f}")
print(f"Benzene p-value: {benzene_p:.6f}")

print(f"Cadmium correlation: {cadmium_r:.4f}")
print(f"Cadmium p-value: {cadmium_p:.6f}")