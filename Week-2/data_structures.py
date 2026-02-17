# Week 2: Data Structures and Functions

# 1. Data Structures
numbers_list = [1, 2, 2, 3, 4, 5, 5, 6]
numbers_tuple = (10, 20, 30)
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
unique_numbers_set = set(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)
print("Dictionary:", student_scores)
print("Set (unique values):", unique_numbers_set)


# 2. Functions and Data Transformations

# Sum of squares using list comprehension
def sum_of_squares(nums):
    squares = [x**2 for x in nums]
    return sum(squares)

print("Sum of squares:", sum_of_squares(numbers_list))


# Filtering using lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
print("Filtered even numbers:", even_numbers)


# 3. Recursion example: factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# 4. Client Project: Data Cleaning Script

raw_data = [12, 15, 12, 20, 25, 20, 30, 35, 30, 40]

# Remove duplicates
cleaned_data = list(set(raw_data))

# Filter values greater than 20
filtered_data = [x for x in cleaned_data if x > 20]

print("\nRaw Data:", raw_data)
print("Cleaned Data (duplicates removed):", cleaned_data)
print("Filtered Data (values > 20):", filtered_data)
