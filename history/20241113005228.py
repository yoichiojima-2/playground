# Here, I will create a simple Python script that calculates the average of a list of numbers

def calculate_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

# Test the function with a list of numbers
numbers = [5, 10, 15, 20, 25]
average = calculate_average(numbers)
print("The average is:", average)
