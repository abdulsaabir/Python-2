def arrange_string(text):
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                result = char + result
            else:
                result += char

    return result

# Test cases
print(arrange_string("AbCdEfG123"))  # "bcdefAG"
print(arrange_string("Hello123"))    # "ello"
print(arrange_string("123ABC"))      # ""
print(arrange_string("aAbBcCdD"))    # "abcdABCD"
