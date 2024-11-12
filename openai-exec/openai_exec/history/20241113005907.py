# Define a function that generates a random password with a given length
import random
import string

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return password

# Generate a random password with length 12
random_password = generate_password(12)
print(random_password)  # Output the random password
