# Original Python Script
for i in range(1, 6):
    print(i)

# Improved Python Script
numbers = [i for i in range(1, 6)]  # Using list comprehension to generate numbers
print(*numbers)  # Using unpacking operator to print numbers without brackets
