# we will use this as sample string for demonstration
sample_string = "Hello, World! This is an example string."

# capitalize() - Converts the first character to upper case
capitalized = sample_string.capitalize()
print(capitalized)  # Hello, world! this is an example string.

# casefold() - Converts string into lower case
casefolded = sample_string.casefold()
print(casefolded)  # hello, world! this is an example string.

# count() - Returns the number of times a specified value occurs in a string
count_occurrences = sample_string.count('l')
print(count_occurrences)  # 3

# endswith() - Returns true if the string ends with the specified value
ends_with = sample_string.endswith("string.")
print(ends_with)  # True

# find() - Searches the string for a specified value and returns the position of where it was found
position = sample_string.find("World")
print(position)  # 7

# index() - Searches the string for a specified value and returns the position of where it was found
position_index = sample_string.index("World")
print(position_index)  # 7

# isalnum() - Returns True if all characters in the string are alphanumeric (A-Z) and (0-9)
is_alphanumeric = sample_string.isalnum()
print(is_alphanumeric)  # False

# isalpha() - Returns True if all characters in the string are in the alphabet (A-Z)
is_alpha = sample_string.isalpha()
print(is_alpha)  # False  


# isdecimal() - Returns True if all characters in the string are decimals (0-9)
is_decimal = "12345".isdecimal()
print(is_decimal)  # True

# isdigit() - Returns True if all characters in the string are digits (0-9) also returns True for ome other Unicode-supported chars 
is_digit = "12345".isdigit()
print(is_digit)  # True

# islower() - Returns True if all characters in the string are lower case
is_lower = sample_string.islower()
print(is_lower)  # False

# isnumeric() - Returns True if all characters in the string are numeric 
#  numeric characters, including not only decimal digits (0-9) but also other numeric characters like fractions, subscripts, superscripts, and characters from different numeral systems. For example, "½²١٢٣" would return True.
is_numeric = "١٢٣".isnumeric() 
print(is_numeric, 'yes it is numeric')  # True

# isspace() - Returns True if all characters in the string are whitespaces
is_space = ' '.isspace()
print(is_space)  # True

# istitle() - Returns True if the string follows the rules of a title 
# The first character of each word should be in uppercase., All other characters in the word should be in lowercase.
is_title = "This Is A Title".istitle()
print(is_title)  # True

# isupper() - Returns True if all characters in the string are upper case (A-Z)
is_upper = sample_string.isupper()
print(is_upper)  # False

# lower() - Converts a string into lower case
lower_case = sample_string.lower()
print(lower_case)  # hello, world! this is an example string.

# lstrip() - Returns removed spaces from left of the string
left_stripped = "   Left strip".lstrip()
print(left_stripped)  # Left strip


# replace() - Returns a string where a specified value is replaced with a specified value
replaced = sample_string.replace("World", "Universe")
print(replaced)  # Hello, Universe! This is an example string.

# rfind() - Searches the string for a specified value and returns the last position of where it was found
last_position = sample_string.rfind("example")
print(last_position)  # 18

# rindex() - Searches the string for a specified value and returns the last position of where it was found
last_index = sample_string.rindex("example")
print(last_index)  # 18


# rstrip() - Returns removed spaces from right of the string
right_stripped = "Right strip   ".rstrip()
print(right_stripped)  # Right strip

# starts_with() - Returns true if the string starts with the specified value
starts_with = sample_string.startswith("Hello")
print(starts_with)  # True

# strip() - Returns a removed white spaces from right and left of the string
stripped = "   Strip   ".strip()
print(stripped)  # Strip

# swapcase() -returns Swaps cases, lower case becomes upper case and upper cases becomes lower case
swapped_case = sample_string.swapcase()
print(swapped_case)  # hELLO, wORLD! tHIS IS AN EXAMPLE STRING.

# title() - Converts the first character of each word to upper case
title_case = "this is a title".title()
print(title_case)  # This Is A Title

# upper() - Converts a string into upper case
upper_case = sample_string.upper()
print(upper_case)  # HELLO, WORLD! THIS IS AN EXAMPLE STRING.