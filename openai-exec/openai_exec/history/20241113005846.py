# Python code to find the sum of all even numbers in a list

def sum_of_even_numbers(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return sum(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers)
print(result)
```

Expected stdout:
```
30
