# This code takes a list of numbers, squares each number, and returns the sum of all squared numbers

def sum_of_squares(numbers):
    if numbers is None:  # Check if the input is None
        return None

    squared_numbers = [num**2 for num in numbers]  # Square each number in the list
    total = sum(squared_numbers)  # Calculate the sum of squared numbers

    return total

# Test the function with a list of numbers
result = sum_of_squares([1, 2, 3, 4, 5])
print(result)
