# This code calculates the Fibonacci sequence up to a specified number of terms

def fibonacci(n):
    sequence = []
    
    # Adding the first two terms 0 and 1
    sequence.append(0)
    sequence.append(1)
    
    for i in range(2, n):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)
    
    return sequence

n = 10
fib_series = fibonacci(n)
print(f"The Fibonacci sequence up to {n} terms is: {fib_series}")
```

**Expected Output:**
```
The Fibonacci sequence up to 10 terms is: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
