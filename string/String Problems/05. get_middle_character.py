def get_middle_characters(input_string):
    length = len(input_string)

    if length % 2 == 0:  # String has an even length
        middle_start = length // 2 - 1
        middle_end = length // 2 + 1
        return input_string[middle_start:middle_end]
    else:  # String has an odd length
        middle = length // 2
        return input_string[middle]

# Example usage:
input_string1 = "Hello"
input_string2 = "Python"

result1 = get_middle_characters(input_string1)
result2 = get_middle_characters(input_string2)

print(result1)  # Output will be "l"
print(result2)  # Output will be "th"
