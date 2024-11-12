# Python code that generates the Fibonacci sequence up to the 10th term

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

output = fibonacci(10)
print(output)
