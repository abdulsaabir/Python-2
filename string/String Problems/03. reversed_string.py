def reverse_string(input_str):
    # Initialize an empty string to store the reversed result.
    reversed_str = ""

    # Iterate through the characters of the input string in reverse order.
    for char in input_str:
        # Prepend each character to the reversed string.
        reversed_str = char + reversed_str

    # Return the reversed string.
    return reversed_str


reversed_str = reverse_string("Hello, World!")
print(reversed_str)  # This will print "!dlroW ,olleH" to the console

# Try it out with different words to see how the function works.
# You can call the function and pass it your own words below this comment.