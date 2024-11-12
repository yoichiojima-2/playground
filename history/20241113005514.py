import random

# Generate a 10x10 grid with random numbers from 1 to 10
grid = [[random.randint(1, 10) for _ in range(10)] for _ in range(10]

# Calculate sum of each row and column
row_sums = [sum(row) for row in grid]
col_sums = [sum(col) for col in zip(*grid)]

print("Generated Grid:")
for row in grid:
    print(row)

print("\nSum of each row:")
for i in range(10):
    print(f"Row {i+1}: {row_sums[i]}")

print("\nSum of each column:")
for i in range(10):
    print(f"Column {i+1}: {col_sums[i]}")
