# Week 1: Introduction to Python Programming
# Covers: variables, data types, operators, input/output, conditionals, loops

def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)


def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)

    if b != 0:
        print("Quotient:", a / b)
    else:
        print("Division by zero is not allowed.")


def average_temperature():
    temps = []
    n = int(input("How many temperature readings do you want to enter? "))

    for i in range(n):
        temp = float(input(f"Enter temperature {i+1}: "))
        temps.append(temp)

    avg = sum(temps) / len(temps)
    print("Average Temperature:", avg)


while True:
    print("\n--- Week 1 Python Basics Menu ---")
    print("1. Temperature Converter (Celsius to Fahrenheit)")
    print("2. Calculator")
    print("3. Average Temperature Calculator")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        temperature_converter()
    elif choice == "2":
        calculator()
    elif choice == "3":
        average_temperature()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
