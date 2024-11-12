# This code aims to generate a creative pattern using loops and list manipulation

# Define the size of the pattern
size = 5

# Create a list of initial values for the pattern
pattern = [[0 for _ in range(size)] for _ in range(size)]

# Update the values in the pattern list to create a diagonal pattern
for i in range(size):
    pattern[i][i] = 1

# Display the updated pattern
for row in pattern:
    print(' '.join(map(str, row)))
