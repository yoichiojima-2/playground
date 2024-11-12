# I implemented a more concise and elegant recursive solution to generate the Fibonacci sequence up to the 10th term

def fibonacci(n, fib_sequence=[0, 1]):
    if n == len(fib_sequence):
        return fib_sequence
    else:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        return fibonacci(n, fib_sequence)

output = fibonacci(10)
print(output)

# Output will be the Fibonacci sequence up to the 10th term generated recursively
# This improvement provides a more compact and elegant way of generating the Fibonacci sequence. 

# expected-output
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
