# I will enhance the code by adding a feature that also calculates the product of all odd numbers in the list, and returns both the sum of squares of even numbers and the product of odd numbers.


def calculate_sum_and_product(numbers):
    sum_of_squares_even = 0
    product_of_odds = 1

    for num in numbers:
        if num % 2 == 0:
            sum_of_squares_even += num**2
        else:
            product_of_odds *= num

    return sum_of_squares_even, product_of_odds


# Test the function with a sample list of numbers
numbers = [1, 2, 3, 4, 5, 6]
result_sum, result_product = calculate_sum_and_product(numbers)
print("Sum of squares of even numbers:", result_sum)
print("Product of odd numbers:", result_product)

# This code now calculates the sum of the squares of even numbers and the product of odd numbers.
