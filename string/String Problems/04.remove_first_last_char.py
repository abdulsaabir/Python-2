def remove_first_and_last_char(input_string):
    if len(input_string) < 2:
        return "String too short"
    else:
        return input_string[1:-1]

# Example usage:
original_string = "Hello, World!"
result = remove_first_and_last_char(original_string)
print(result)  # Output will be "ello, World"
