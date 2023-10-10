# version 1
# Prompt user for two integers
x = input("What's x? ")
y = input("What's y? ")

# Print sum
z = x + y
print(z)



# version 2
# Demonstrates conversion from str to int
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)


# version 3
# Demonstrates nesting of function calls
x = int(input("What's x? "))
y = int(input("What's y? "))

z = x + y

print(z)


# version 4 
# Demonstrates division with float
x = input("What's x? ")
y = input("What's y? ")

z = round(x / y)

print(z)

# version 5
# Demonstrates division with float and round two digits
x = input("What's x? ")
y = input("What's y? ")

z = round(x / y, 2)

print(z)

