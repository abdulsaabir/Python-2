def replace_char(text, old_char, new_char):
    if old_char in text:
        replaced_text = text.replace(old_char, new_char)
        return replaced_text
    else:
        return f"The character '{old_char}' was not found in the text."



# Example 1:
print(replace_char("Hello, World!", "o", "$"))  # Output will be "Hell$, W$rld!"

# Example 2:
result2 = replace_char("Python is fun!", "x", "@")
print(result2)  # Output will be "The character 'x' was not found in the text."
