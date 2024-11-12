# This code reads a list of numbers and calculates the sum of even numbers

# Read a list of numbers separated by space
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

# Initialize a variable to store the sum of even numbers
even_sum = 0

# Calculate the sum of even numbers in the list
for num in numbers:
    if num % 2 == 0:
        even_sum += num

# Print the sum of even numbers
print(f"Sum of even numbers: {even_sum}")
