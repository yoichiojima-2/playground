# Creating a fun and creative script that generates a random joke using the random module
import random

# Define a list of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common... it’s a shame they’ll never meet.",
    "I told my wife she should embrace her mistakes... She gave me a hug.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book on anti-gravity, it's impossible to put down!"
]

# Select a random joke from the list
random_joke = random.choice(jokes)
print(random_joke)
