# The code takes a list of numbers, calculates the sum of all elements, and returns the result
def calculate_sum(num_list):
    # Check if the num_list is not empty
    if num_list:
        return sum(num_list)
    else:
        return "List is empty"

# Test the function with the provided list of numbers
result = calculate_sum([10, 20, 30, 40, 50])
print(result)
