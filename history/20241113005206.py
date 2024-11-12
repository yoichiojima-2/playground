# This code creates a function that generates a random quote from a list of quotes.

import random

def generate_quote():
    quotes = [
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "Do one thing every day that scares you. -Eleanor Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. -Confucius",
        "Happiness is not something ready made. It comes from your own actions. -Dalai Lama",
        "The only way to do great work is to love what you do. -Steve Jobs"
    ]

    random_quote = random.choice(quotes)
    return random_quote

# Testing the function
print(generate_quote())
