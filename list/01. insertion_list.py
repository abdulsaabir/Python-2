# Create the first list
first_list = [1, 2, 3, 4, 5]


# ------------ len function ------------------
# Use len() to get the length of the list
list_length = len(first_list)
print("First List:", first_list)
print("Length of the first list:", list_length)


# ------------------------- indexing and slicing --------------------
# Indexing and slicing examples
first_element = first_list[0]  # Access the first element (1)
print("First Element:", first_element)

second_element = first_list[1]  # Access the second element (2)
print("Second Element:", second_element)

last_element = first_list[-1]   # Access the last element (5)
print("Last Element (Negative Indexing):", last_element)

# Slicing examples
slice1 = first_list[1:4]      # Slice from index 1 to 3 ([2, 3, 4])
print("Sliced List :", slice1)

slice2 = first_list[:3]       # Slice from the beginning to index 2 ([1, 2, 3])
print("Sliced List ", slice2)

slice3 = first_list[2:]       # Slice from index 2 to the end ([3, 4, 5])
print("Sliced List ", slice3)

slice4 = first_list[::2]      # Slice every second element ([1, 3, 5])
print("Sliced List :", slice4)




# ---------------- append ---------------------
# Create the second list
second_list = []

# Append and print after each operation
second_list.append(6)
print("Second List After Appending 6:", second_list)

second_list.append(7)
print("Second List After Appending 7:", second_list)



# ------------------ append vs extend -------------------

# Create the third list
third_list = [8, 9]

# Append a list to demonstrate the difference and print
third_list.append([10, 11])
print("Third List After Appending:", third_list)  # [8, 9, [10, 11]]

# Create the fourth list
fourth_list = [8, 9]

# Extend with another list and print
third_list.extend([10, 11])
print("Third List After Extending:", third_list)    # [8, 9, 10, 11]

# When using append, it adds one element at the end of the list. If you use append while passing a list, it adds the entire list as a single element within the original list.
# However, if you use extend while passing a list, it adds each element individually at the end of the list.




# --------------- insert ------------------------------
# Create the fifth list
fifth_list = [1, 2, 4, 5]

# Print the original list
print("Fifth List (Original):", fifth_list)

# Use the insert method to add an element at a specific index
fifth_list.insert(2, 3)  # 2 is the position (index) to add and 3 is the element to add
print("new list after adding 3 in the 2nd index is :", fifth_list)

# The insert method takes two arguments:
# - The first argument is the index where the element should be inserted.
# - The second argument is the element to be inserted.


