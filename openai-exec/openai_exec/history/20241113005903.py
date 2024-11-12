# Creatively combining list comprehension and ternary operator to generate a unique output

result = [x**2 if x % 2 == 0 else x**3 if x % 3 == 0 else x for x in range(1, 11)]
print(result)
