def remove_special_symbols(input_string):
    cleaned_string = ""  # Initialize an empty string to store the cleaned result

    for char in input_string:
        if char.isalnum():  # Check if the character is alphanumeric (letter or digit)
            cleaned_string += char  # Append the character to the cleaned string

    return cleaned_string

# Test cases
input_str = "Hello, World! This is a test 123."
result = remove_special_symbols(input_str)
print(result)
