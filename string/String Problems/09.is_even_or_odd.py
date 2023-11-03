def is_even_or_odd(input_str):
    if input_str.isdigit():
        number = int(input_str)
        if number % 2 == 0:
            return True  # It's even
        else:
            return False  # It's odd
    else:
        return "Input is not a digit."

# Example usage:
print(is_even_or_odd("4"))      # True
print(is_even_or_odd("7"))      # False
print(is_even_or_odd("3"))      # False
print(is_even_or_odd("12345"))  # False
print(is_even_or_odd("100"))    # True
print(is_even_or_odd("abc"))    # Input is not a digit.
