# This code generates a list of Fibonacci numbers up to a given limit in a creative way by using a recursive function

def fibonacci_list(limit, a=0, b=1, lst=None):
    # Initialize the list if it's None
    if lst is None:
        lst = []

    # Base case: if the limit is 0, return an empty list
    if limit == 0:
        return []

    # Add the next Fibonacci number to the list
    next_number = a + b
    lst.append(a)

    # Recursive call with updated parameters
    if limit > 1:
        fibonacci_list(limit - 1, b, next_number, lst)

    return lst

# Call the function to generate Fibonacci numbers up to the limit of 10
result = fibonacci_list(10)
print(result)
