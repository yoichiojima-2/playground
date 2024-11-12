# This code generates a random password with a length specified by the user
import random
import string

def generate_password(length):
    if length < 8:
        return "Password length should be at least 8 characters"
    else:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        return password

# Customized function to generate a random password that is at least 12 characters long
def generate_strong_password():
    password = generate_password(random.randint(12, 20))  # Generating a password between 12 to 20 characters
    return password

# Using the customized function to generate a strong password
strong_password = generate_strong_password()
print(strong_password)
