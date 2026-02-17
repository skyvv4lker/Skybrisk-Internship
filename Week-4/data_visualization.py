# Week 4: Data Visualization with Matplotlib and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    "day": [1, 2, 3, 4, 5, 6, 7],
    "temperature": [32, 34, 33, 31, 35, 36, 34],
    "humidity": [60, 58, 62, 65, 55, 50, 57]
}

df = pd.DataFrame(data)


# Basic Plots with Matplotlib

# Line plot: Temperature vs Day
plt.figure()
plt.plot(df["day"], df["temperature"], marker="o")
plt.title("Temperature Over Days")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.savefig("temperature_line_plot.png")
plt.show()

# Histogram: Temperature distribution
plt.figure()
plt.hist(df["temperature"], bins=5)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.savefig("temperature_histogram.png")
plt.show()


# Advanced Plots with Seaborn

# Scatter plot: Temperature vs Humidity
plt.figure()
sns.scatterplot(x="temperature", y="humidity", data=df)
plt.title("Temperature vs Humidity")
plt.savefig("temp_vs_humidity_scatter.png")
plt.show()

# Heatmap: Correlation between features
plt.figure()
corr = df[["temperature", "humidity"]].corr()
sns.heatmap(corr, annot=True)
plt.title("Feature Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

# Pairplot (Dashboard-style overview)
sns.pairplot(df)
plt.savefig("pairplot_dashboard.png")
plt.show()
