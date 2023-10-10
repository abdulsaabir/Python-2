# version 1
# Prints a column of bricks
print("#")
print("#")
print("#")


# version 2
# Prints column of bricks using a loop
for _ in range(3):
    print("#")


# version 3
# Prints row of bricks using a loop
for _ in range(3):
    print("#", end='')



# version 3
# prints row and column of bricks using loop
for _ in range(3):
    print("###")


# version 4
for i in range(1,5):
    for j in range(i):
        print("#", end="")
    print()



