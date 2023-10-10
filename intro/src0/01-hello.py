# version 1
name = input("What's your name? ")
print("hello, " + name)

#version 2
name = input("What's your name? ")
print("hello, ", name)

# version 3 
name = input("What's your name? ")
print("hello,", name, end="",)

# version 4
name = input("What's your name? ")
print(f"hello, {name}")

# version 5
name = input("What's your name? ")
name = name.strip()
# name = name.capitalize()
# name = name.upper()
print(f"hello, {name}")

