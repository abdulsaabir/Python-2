def sum_positives_and_negatives(numbers):
    positive_sum = 0
    negative_sum = 0

    for x in numbers:
        if x > 0:
            positive_sum += x
        elif x < 0:
            negative_sum += x

    return [positive_sum, negative_sum]

# Example usage:
numbers = [1, -2, 3, -4, 5]
result = sum_positives_and_negatives(numbers)
print("Sum of positives and negatives:", result)
