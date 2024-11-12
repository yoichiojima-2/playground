def generate_magic_number():
    import random
    return random.randint(1, 100)

magic_number = generate_magic_number()
print(f"The magic number is: {magic_number}")
