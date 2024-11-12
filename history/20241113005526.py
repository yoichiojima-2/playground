# Generate a list of even numbers using list comprehension
# Added more functionality to take input from the user for the limit of even numbers

try:
    limit = int(input("Enter the limit for even numbers: "))
    even_numbers = [num for num in range(1, limit + 1) if num % 2 == 0]

    if even_numbers:
        print(f"Even numbers up to {limit}: {even_numbers}")
    else:
        print("No even numbers found.")

except ValueError:
    print("Please enter a valid integer as the limit.")
except Exception as e:
    print(f"An error occurred: {e}")
