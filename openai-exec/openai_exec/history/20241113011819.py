# Improved is_prime function that checks for even numbers
# and optimizes the loop iteration by checking only odd numbers
def is_prime(num):
    if num < 2:
        return False
    if num < 4:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# fibonacci function remains the same

fib_numbers = fibonacci(1000)
prime_sum = sum(num for num in fib_numbers if is_prime(num))

print(prime_sum)
```

[result-output]
345
