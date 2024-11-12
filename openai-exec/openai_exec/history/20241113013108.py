# Here, I'm going to create a program that takes a list of numbers and calculates the sum of the squares of all even numbers in the list.


def sum_of_squares_of_even_numbers(numbers):
    sum = 0

    for num in numbers:
        if num % 2 == 0:
            sum += num**2

    return sum


# Test the function with a sample list of numbers
numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_squares_of_even_numbers(numbers)
print(result)
