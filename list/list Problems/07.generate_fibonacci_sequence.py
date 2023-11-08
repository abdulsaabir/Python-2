def generate_fibonacci_sequence(initial_numbers, count):
    if count <= 1:
        return []

    sequence = initial_numbers

    while len(sequence) < count:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Example usage:
fib_sequence = generate_fibonacci_sequence([1, 2], 10)  # Pass the initial numbers and count directly
print("Fibonacci Sequence:")
print(fib_sequence)
