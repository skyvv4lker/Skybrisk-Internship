# Week 3: NumPy and Pandas for Data Manipulation

import numpy as np
import pandas as pd


# 1. NumPy: Arrays, Operations, Broadcasting

arr = np.array([10, 20, 30, 40, 50])
print("NumPy Array:", arr)

# Basic operations
print("Array + 5 (broadcasting):", arr + 5)
print("Array * 2:", arr * 2)
print("Mean of array:", np.mean(arr))


# 2. Pandas: DataFrame, Series, Indexing

data = {
    "day": [1, 2, 3, 4, 5, 6],
    "temperature": [32, 34, None, 31, 35, None],
    "city": ["Delhi", "Delhi", "Delhi", "Delhi", "Delhi", "Delhi"]
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

# Series example
temp_series = df["temperature"]
print("\nTemperature Series:")
print(temp_series)

# Indexing
print("\nFirst 3 rows using indexing:")
print(df.iloc[:3])


# 3. Client Project: Data Cleaning & Aggregation

# Remove missing values
cleaned_df = df.dropna()
print("\nDataFrame after removing missing values:")
print(cleaned_df)

# Grouping & aggregation (average temperature by city)
avg_temp_by_city = cleaned_df.groupby("city")["temperature"].mean()

print("\nAverage Temperature by City:")
print(avg_temp_by_city)
