# I will attempt to create a unique pattern based on the provided output "None"

# Generating a diamond pattern with "*"
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
