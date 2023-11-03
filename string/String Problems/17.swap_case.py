

# SOLUTION 1 THE LONG WAY 

def swap_case(input_string):
    swapped_string = ""

    for char in input_string:
        if char.isalpha():
            if char.islower():
                swapped_string += char.upper()
            else:
                swapped_string += char.lower()
        else:
            swapped_string += char

    return swapped_string

# Test cases
input_str = "Hello, World! This is a Test 123."
result = swap_case(input_str)
print(result)




# SOLUTION 2 THE SHORT WAY 

def swap_case(input_string):
    return input_string.swapcase()  # swapcase is string method that Swaps the case of alphabet.


# Test cases
input_str = "Hello, World! This is a Test 123."
result = swap_case(input_str)
print(result)
