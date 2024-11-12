# This script will create a list of numbers where each number is the sum of the two numbers that came before it

def generate_sequence(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_num = sequence[i-1] + sequence[i-2]
            sequence.append(next_num)
        return sequence

# Generate the sequence of numbers
result = generate_sequence(10)
print(result)
