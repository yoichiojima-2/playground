# Goal of this code is to find the maximum value in a list of numbers in a creative way

numbers = [3, 7, 2, 9, 12, 4, 6, 8]

# Using a lambda function to find the maximum value in the list
max_num = max(numbers, key=lambda x: x if x % 2 == 0 else float('-inf'))

print(max_num)
