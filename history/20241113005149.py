# Import necessary modules
import math

# Define a function to calculate the area of a circle
def calculate_circle_area(radius):
    if radius >= 0:
        return math.pi * radius ** 2
    else:
        return None

# Prompt user to input radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = calculate_circle_area(radius)

# Check if the area is calculated successfully and print the result
if area is not None:
    print(f"The area of the circle with radius {radius} is: {area}")
else:
    print("Please enter a valid radius.")
