# The code below generates a list of even numbers up to a certain limit provided by the user

def generate_even_numbers(limit):
    if limit < 0:
        return None
    
    even_numbers = [num for num in range(0, limit + 1) if num % 2 == 0]
    
    return even_numbers

# Let's test the function with a limit of 10
result = generate_even_numbers(10)

print(result)
