# Example 1: Using a for loop without enumerate
fruits = ["apple", "banana", "cherry", "date"]

# Loop through the list elements without using enumerate
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
# date

# Example 2: Using a for loop with enumerate
fruits = ["apple", "banana", "cherry", "date"]

# Loop through the list elements with enumerate
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry
# Index 3: date


"""
The difference:

- In Example 1, a for loop is used without enumerate. It iterates through the elements of the list directly.

- In Example 2, a for loop with enumerate is used. It provides both the index of the element  and the element itself in each iteration.

- Using enumerate is helpful when you need to access both the index and the element within the loop.

"""