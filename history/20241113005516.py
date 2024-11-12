# Define a function to create a list of odd numbers up to a given limit
def generate_odd_numbers(limit):
    odd_numbers = [num for num in range(1, limit+1) if num % 2 != 0]
    return odd_numbers

# Call the function and print the result
result = generate_odd_numbers(10)
print(result)
