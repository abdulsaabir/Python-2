def add_ing_or_ly(text):
    if len(text) < 3:
        return text  # Leave it unchanged if the length is less than 3
    if text.endswith('ing'):
        return text + 'ly'  # Add 'ly' if it already ends with 'ing'
    else:
        return text + 'ing'  # Add 'ing' otherwise

# Test cases
print(add_ing_or_ly("jump"))      # "jumping"
print(add_ing_or_ly("swimming"))  # "swimmingly"
print(add_ing_or_ly("do"))        # "do"
print(add_ing_or_ly("coding"))    # "codingly"
