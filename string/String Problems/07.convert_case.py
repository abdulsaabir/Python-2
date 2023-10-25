def convert_case(text):
    # if text and text[0].isupper():
    if text[0].isupper():
        return text.upper()
    else:
        return text.lower()

# Example usage:
result1 = convert_case("Hello, World!")
result2 = convert_case("python is great")

print(result1)  # Output will be "HELLO, WORLD!"
print(result2)  # Output will be "python is great"
