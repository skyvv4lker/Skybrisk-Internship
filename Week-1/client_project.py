# Client Project - Week 1
# Basic Data Processing Script: Average Temperature Calculation

def calculate_average_temperature():
    temperatures = []

    n = int(input("Enter the number of temperature readings: "))

    for i in range(n):
        temp = float(input(f"Enter temperature reading {i + 1}: "))
        temperatures.append(temp)

    total = 0
    for t in temperatures:
        total += t

    average = total / len(temperatures)

    print("\nTemperature Readings:", temperatures)
    print("Average Temperature:", average)


if __name__ == "__main__":
    calculate_average_temperature()
