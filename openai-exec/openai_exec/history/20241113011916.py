# Original Python Script
for i in range(1, 6):
    print(i)

# Improved Python Script
numbers = [i for i in range(1, 6)]  # Using list comprehension to generate numbers
print(*numbers)  # Using unpacking operator to print numbers without brackets

# The original script printed each number on a new line, 
# the improved script generates numbers in a list using list comprehension 
# and then prints them separated by spaces using the unpacking operator.
