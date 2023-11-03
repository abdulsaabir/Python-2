# Example: Using 'in' and 'not in' to check for the presence of an element in a list
fruits = ["apple", "banana", "cherry", "date"]

# Check if "banana" is in the list
if "banana" in fruits:
    print("Banana is in the list.")
else:
    print("Banana is not in the list.")

# Output: Banana is in the list.

# Check if "grape" is not in the list
if "grape" not in fruits:
    print("Grape is not in the list.")
else:
    print("Grape is in the list.")

# Output: Grape is not in the list.
"""
the difference:

- 'in' checks if an element is present in the list and returns True if it is and returns false if the element is not present in the list

- 'not in' checks if an element is not present in the list and returns True if the element is not in the list , but if the element is in the list it returns False.

- These operators are used for membership testing in lists.
"""
