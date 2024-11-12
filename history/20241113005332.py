# Here, I'm creating a list of colors and then printing each color along with its length
colors = ['red', 'blue', 'green', 'yellow']

# Using a list comprehension to print each color along with its length in a creative way
print('\n'.join(f"{color} - Length: {len(color)}" for color in colors))
