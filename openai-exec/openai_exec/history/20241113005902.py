# This code takes a list of integers, squares each number, and then sums all the squared values
def square_and_sum(nums):
    if isinstance(nums, list):
        squared_nums = [num**2 for num in nums]
        total = sum(squared_nums)
        return total
    else:
        return "Input must be a list of numbers"

# Example list of numbers
numbers = [1, 2, 3, 4, 5]
result = square_and_sum(numbers)
print(result)
