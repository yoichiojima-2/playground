# The goal of this code is to generate a Fibonacci sequence with a twist for a given number of terms

# Function to generate Fibonacci sequence with a twist
def fibonacci_with_twist(n):
    # Check if n is negative
    if n <= 0:
        return "Number of terms should be a positive integer"
    
    # Initialize Fibonacci sequence with first two terms
    fib_sequence = [0, 1]
    
    # Generate Fibonacci sequence with a twist for the given number of terms
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + 2 * fib_sequence[i - 2]  # Fibonacci sequence with a twist
        fib_sequence.append(next_term)
    
    return fib_sequence

# Number of terms for the Fibonacci sequence
num_terms = 10

# Generate Fibonacci sequence with a twist for the given number of terms
result = fibonacci_with_twist(num_terms)
print(result)
