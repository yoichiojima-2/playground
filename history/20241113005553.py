# This program generates a random pattern of stars on the console

import random

def generate_stars_pattern(rows, cols, density):
    for _ in range(rows):
        row = ""
        for _ in range(cols):
            if random.random() < density:
                row += "*"
            else:
                row += " "
        print(row)

# Setting the parameters for the star pattern
num_rows = 10
num_cols = 20
star_density = 0.5

# Generate the star pattern
generate_stars_pattern(num_rows, num_cols, star_density)
