# Week 3 Client Project
# Clean and aggregate a dataset using Pandas

import pandas as pd

def main():
    # Sample dataset with missing values
    data = {
        "day": [1, 2, 3, 4, 5, 6],
        "temperature": [32, None, 34, 31, None, 35],
        "city": ["Delhi", "Delhi", "Delhi", "Delhi", "Delhi", "Delhi"]
    }

    df = pd.DataFrame(data)

    print("Original Dataset:")
    print(df)

    # Step 1: Remove missing values
    cleaned_df = df.dropna()

    print("\nDataset after removing missing values:")
    print(cleaned_df)

    # Step 2: Aggregate data (calculate average temperature per city)
    avg_temperature = cleaned_df.groupby("city")["temperature"].mean()

    print("\nAverage Temperature by City:")
    print(avg_temperature)


if __name__ == "__main__":
    main()
