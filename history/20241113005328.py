# This code generates a random password with a mixture of uppercase letters, lowercase letters, numbers, and special characters.

import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a random password of length 12
password = generate_random_password(12)
print(password)
