# We will create a function that generates a list of random numbers and returns the maximum value in the list

import random

def get_max_value(num_elements):
    # Generate a list of random numbers
    random_numbers = [random.randint(1, 100) for _ in range(num_elements)]
    print("List of random numbers:", random_numbers)
    
    # Find the maximum value in the list
    max_value = max(random_numbers) if random_numbers else None
    return max_value

# Call the function and print the maximum value
max_value = get_max_value(5)
print("Maximum value in the list:", max_value)
