# Week 4 Client Project
# Dashboard for Visualizing Relationships Between Features

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


# Histogram: Distribution of Temperature
plt.figure()
plt.hist(df["temperature"], bins=5)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.savefig("dashboard_temperature_histogram.png")
plt.show()


# Scatter Plot: Temperature vs Humidity
plt.figure()
sns.scatterplot(x="temperature", y="humidity", data=df)
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("dashboard_temp_vs_humidity_scatter.png")
plt.show()


# Scatter Plot: Day vs Temperature
plt.figure()
plt.scatter(df["day"], df["temperature"])
plt.title("Day vs Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.savefig("dashboard_day_vs_temperature_scatter.png")
plt.show()
