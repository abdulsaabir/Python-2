def factorial(num):
    if str(num).isdigit():
        num = int(num)
        if num >= 0:
            result = 1
            for i in range(num, 1, -1):
                result *= i
            return result
    return "Input must be a positive number (integer or string)."

# Test cases
print(factorial(4))      # 24
print(factorial("4"))    # 24
print(factorial(0))      # 1
print(factorial(5))      # 120
print(factorial("7"))    # 5040
print(factorial(-3))     # Input must be a positive number
print(factorial("abc"))  # Input must be a positive number (integer or string).
