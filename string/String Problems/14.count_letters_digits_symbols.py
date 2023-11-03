def count_letters_digits_symbols(text):
    letters = 0
    digits = 0
    symbols = 0

    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    print(f"Letters: {letters}")
    print(f"Digits: {digits}")
    print(f"Symbols: {symbols}")

# Test cases
count_letters_digits_symbols("Hello, World! 123")
# Expected output:
# Letters: 10
# Digits: 3
# Symbols: 3

count_letters_digits_symbols("Testing 123")
# Expected output:
# Letters: 7
# Digits: 3
# Symbols: 0

count_letters_digits_symbols("$$$Money$$$")
# Expected output:
# Letters: 5
# Digits: 0
# Symbols: 6

count_letters_digits_symbols("1234567890")
# Expected output:
# Letters: 0
# Digits: 10
# Symbols: 0

count_letters_digits_symbols("AaBbCc 12345 !@#$%^")
# Expected output:
# Letters: 6
# Digits: 5
# Symbols: 7
