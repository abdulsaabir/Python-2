def modify_first_char_occurrences(input_text, symbol):
    if len(input_text) < 2:
        return input_text  # Cannot modify if the text has only one character or is empty

    first_char = input_text[0]
    modified_text = first_char

    for char in input_text[1:]:
        if char.lower() == first_char.lower():
            modified_text += symbol
        else:
            modified_text += char

    return modified_text

# Test cases
print(modify_first_char_occurrences("HTML", "$"))  # "$TML"
print(modify_first_char_occurrences("restaurRant", "$"))  # "res$taurant"


