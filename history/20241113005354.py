# This code generates a list of random numbers and calculates the sum of all even numbers in the list
import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Filter even numbers from the list and calculate their sum
even_sum = sum(num for num in random_numbers if num % 2 == 0)

even_sum # Returning the sum of even numbers
