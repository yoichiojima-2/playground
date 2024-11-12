# This code snippet generates a random password with a mix of uppercase letters, lowercase letters, digits, and symbols.

import string
import random

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = generate_password()
print(password)
