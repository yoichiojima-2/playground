# This program generates a random password of a specified length

import random
import string

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    return password

# For added security, the password now includes special characters
def generate_secure_password(length):
    secure_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return secure_password

# Let's create a secure password of length 12
result = generate_secure_password(12)
print(result)  # Print the generated secure password
