# Original Python Script - Generates a random number and prints it
import random

random_number = random.randint(1, 100)
print(f"The random number is: {random_number}")
```

```python
# Improved Python Script - Generates a random number and prints it as a colorful message
import random

# Generate a random number
random_number = random.randint(1, 100)

# Print the random number in a colorful message
print("\033[1;36;40m")  # Set text color to cyan
print(f"---- Random Number Generator ----")
print(f"| The random number is: \033[1;31;40m{random_number}\033[1;36;40m |")
print("--------------------------------")
print("\033[0;37;40m")  # Reset text color to default
```

```python
# Result Output
---- Random Number Generator ----
| The random number is: 42 |
--------------------------------
