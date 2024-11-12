# I will create a function that simulates a magic eight ball
import random

def magic_eight_ball():
    # Possible answers
    answers = ["Yes", "No", "Maybe", "Try again later", "Outlook not so good", "Absolutely"]

    # Randomly selecting an answer
    chosen_answer = random.choice(answers)
    
    # Returning the chosen answer
    return chosen_answer

# Let's test the magic eight ball function
print(magic_eight_ball())
