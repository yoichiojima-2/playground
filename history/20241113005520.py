# I will create a simple function that prints a message with some emojis for fun

def greeting():
    emojis = ["😊", "🌟", "🎉"]
    message = "Hello! Welcome to the Python world! Enjoy your coding journey!"
    
    for emoji in emojis:
        print(emoji, end=" ")
    print(message)
    
greeting()
