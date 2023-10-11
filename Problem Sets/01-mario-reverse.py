# The following code repeatedly prompts the user for a valid height input
# until a valid height within the range of 1 to 8 is provided.

while True:
    height = input("Height: ")

    # Check if the input is not a number (contains non-numeric characters) or
    # if it's not within the valid range (1 to 8). If so, continue the loop.
    if height.isalpha() or int(height) < 1 or int(height) > 8:
        continue
    else:
        break  # Exit the loop when a valid height is provided.

# Convert the valid height input to an integer.
height = int(height)

# The following code uses the provided height to print a pyramid pattern.
# It consists of two nested loops for printing spaces and '#' symbols.

for i in range(1, height + 1):  # Loop through each level of the pyramid.
    for j in range(height - i):  # Print spaces to align the pyramid to the right.
        print(' ', end='')
    for k in range(i):  # Print '#' symbols to form the pyramid.
        print('#', end='')

    print('')  # Move to the next line to start a new row in the pyramid.
