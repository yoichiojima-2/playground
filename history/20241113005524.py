# This code generates a pattern of '*' characters in the shape of a diamond

# Define the size of the diamond
size = 5

# Create the top part of the diamond
for i in range(size):
    print(' ' * (size - i - 1) + '*' * (2 * i + 1))

# Create the bottom part of the diamond
for i in range(size - 2, -1, -1):
    print(' ' * (size - i - 1) + '*' * (2 * i + 1))
