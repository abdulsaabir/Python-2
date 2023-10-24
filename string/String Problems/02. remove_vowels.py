def remove_vowels(text):
    # Initialize an empty string to store the result.
    result = ""

    # Define a set of vowels in both uppercase and lowercase.
    vowels = "AEIOU"

    # Iterate through each character in the input text.
    for char in text:
        # Check if the character is not a vowel (i.e., it's a consonant or other character).
        if char.upper() not in vowels:
            # If the character is not a vowel, add it to the result string.
            result += char

    # Return the result string with all vowels removed.
    return result


output_text = remove_vowels("Hello, world")
print(output_text)  # This will print "Hll, Wrld!" to the console

# Try it out with different words to see how the function works.
# You can call the function and pass it your own words below this comment.