# This code checks if a list contains any even numbers and returns True if found, False otherwise

def check_for_evens(numbers):
    return any(num % 2 == 0 for num in numbers)

# Example usage
numbers_list = [1, 3, 5, 7, 9]
result = check_for_evens(numbers_list)
print(result)
