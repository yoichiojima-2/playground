# Python code that generates the Fibonacci sequence up to the 10th term

# Here, I'm using an iterative approach to generate the Fibonacci sequence

def fibonacci(n):
    # Initialize the Fibonacci sequence with the first two terms
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence iteratively up to the nth term
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)

    return fib_sequence

output = fibonacci(10)
print(output)

# Output will be the Fibonacci sequence up to the 10th term generated iteratively
# This improvement allows for a more efficient way of generating Fibonacci sequence using iteration

# expected-output
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

