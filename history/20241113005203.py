# This code takes a list of numbers, filters out odd numbers, squares the remaining even numbers, and returns the total sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out odd numbers using list comprehensions
filtered_numbers = [num for num in numbers if num % 2 == 0]

# Square the even numbers
squared_numbers = [num ** 2 for num in filtered_numbers]

# Calculate the total sum of squared even numbers
total_sum = sum(squared_numbers)

# Output the result
total_sum
