# Creating a class named MagicalCalculator
class MagicalCalculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self

    def subtract(self, num):
        self.result -= num
        return self

    def multiply(self, num):
        self.result *= num
        return self

    def divide(self, num):
        if num == 0:
            print("Error: Cannot divide by zero!")
        else:
            self.result /= num
        return self

# Creating an instance of the MagicalCalculator class
calculator = MagicalCalculator()

# Performing arithmetic operations
result = calculator.add(10).subtract(5).multiply(2).divide(3).result

print(result)  # Printing the final result
