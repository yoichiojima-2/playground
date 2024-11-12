# Let's create a function that generates a random string with a given length

import string
import random

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

random_string = generate_random_string(10)
print(random_string)

# Output: Randomly generated string of length 10
