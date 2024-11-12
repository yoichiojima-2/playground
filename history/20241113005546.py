# This code calculates the sum of even numbers from 1 to 100

# Initialize a variable to store the sum of even numbers
even_sum = 0

# Loop through numbers from 1 to 100
for i in range(1, 101):
    # Check if the number is even
    if i % 2 == 0:
        # If even, add the number to the sum
        even_sum += i

# Print the sum of even numbers from 1 to 100
print(even_sum)
