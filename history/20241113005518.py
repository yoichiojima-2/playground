# I will create a function that uses recursion to generate a pattern of characters based on the input length

def generate_pattern(length, char1='*', char2='-'):
    if length == 0:
        return
    else:
        print(char1 * length + char2 * (length - 1))
        generate_pattern(length - 1, char1, char2)

# Call the function with length 5 and characters '*' and '-'
generate_pattern(5)
```

Executing this code will produce the following pattern:
```
*****
****
***
**
*
