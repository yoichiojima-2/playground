# I tried to create a fun and interactive code that utilizes user input to generate a different output each time

import random

answers = ["Yes", "No", "Maybe", "Ask again later", "Outlook not so good", "Definitely"]

print("Welcome to the Magic 8-Ball!\nAsk a question:")
question = input()

if question.endswith("?"):
    print("Thinking...")
    answer = random.choice(answers)
    print("The Magic 8-Ball says:", answer)
else:
    print("Please ask a question.")

# Returning None as the output
print(None)
