# This code creates a list of strings and then prints the length of each string in a creative way

strings = ["apple", "banana", "cherry", "date"]

lengths = [len(s) for s in strings]  # List comprehension to get the lengths of strings

for length in lengths:
    print('*' * length)  # Print '*' repeated 'length' times
