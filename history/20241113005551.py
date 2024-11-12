# This program takes a list of numbers and returns the sum of elements

# Function to calculate sum of elements in a list
def calculate_sum(numbers):
    total_sum = sum(numbers)  # Using the sum() function to calculate the sum
    return total_sum

# List of numbers
numbers_list = [10, 20, 30, 40, 50]

# Getting the sum of numbers in the list
result = calculate_sum(numbers_list)

# Printing the result
print(result)
