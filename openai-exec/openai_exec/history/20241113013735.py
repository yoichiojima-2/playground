# Python code that generates the Fibonacci sequence up to the 10th term

def fibonacci(n):
    # Using a recursive approach to generate Fibonacci sequence
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

output = [fibonacci(i) for i in range(10)]
print(output)

# Output will be the same as the previous code
# The improvement here is using recursive function to generate Fibonacci sequence
