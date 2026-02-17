# Week 2 Client Project
# Script for Data Cleaning: Removing Duplicates and Filtering Data

def remove_duplicates(data):
    """Remove duplicate values from a list"""
    return list(set(data))


def filter_data(data, threshold):
    """Filter values greater than a given threshold"""
    return [x for x in data if x > threshold]


def main():
    raw_data = [12, 15, 12, 20, 25, 20, 30, 5, 5, 40]

    print("Raw Data:", raw_data)

    # Step 1: Remove duplicates
    cleaned_data = remove_duplicates(raw_data)
    print("After Removing Duplicates:", cleaned_data)

    # Step 2: Filter data (keep values greater than 15)
    filtered_data = filter_data(cleaned_data, 15)
    print("After Filtering (values > 15):", filtered_data)


if __name__ == "__main__":
    main()
