# Provided Python Script
for i in range(1, 6):
    print(i)

# Improved Python Script - Using a generator expression and string formatting
numbers = ' '.join(str(i) for i in range(1, 6))  # Using generator expression for numbers with string formatting
print(numbers)  # Printing numbers as a single string separated by spaces

# In this improved version, a generator expression is used to create a string of numbers
# separated by spaces, which is then printed as a single string.

# Expected Output:
# 1 2 3 4 5
