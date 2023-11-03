# --------- pop ----------
# Removes last element using pop()

# Example 1
list1 = [1, 2, 3, 4, 3, 5]
list1.pop()  # it removes the last element 5 
print("Updated list1 after popping the last element:", list1) #   [1, 2, 3, 4, 3]

# Example 2
list2 = ["apple", "banana", "cherry"]
list2.pop()  # it removes the last fruit cherry
print("Updated list2 after popping the last element:", list2) # ["apple", "banana"]

# Example 3
list3 = [10, 20, 30, 40, 50]
list3.pop()   # it removes the last number 50
print("Updated list3 after popping the last element:", list3)  # [10, 20, 30, 40]





# --------- remove ----------
# Remove the first occurrence of a specific element using remove()


# Example 1
list4 = [1, 2, 3, 4, 3, 5]
list4.remove(3) # it removes the number 3 from the list (the first 3 only) 
print(list4)    # Expected Output:  [1, 2, 4, 3, 5]

# Example 2
list5 = ["apple", "banana", "cherry", "apple"]
list5.remove("apple") #  it removes the fruit apple from the list (the first apple only) 
print(list5)   # Expected Output: ["banana", "cherry", "apple"]

# Example 3
list6 = [10, 20, 30, 20, 40, 50]
list6.remove(20)  # we removed the number 20 from the first (the first 3 only) 
list6.remove(20)  # again we removed the number 20 in the list (now the second 20) 
print(list6)  # Expected Output:  [10, 30, 40, 50]






# --------- pop with index ----------
# Remove and return an element at a specific index using pop(index)


# Example 1
list7 = [1, 2, 3, 4, 5]
list7.pop(1) # we removing the element at index (1) which is number 2
print(list7)  # Expected Output:[1, 3, 4, 5]

# Example 2
list8 = ["apple", "banana", "cherry"]
list8.pop(0)  # we removing the fruit at index (0) which is apple
print(list8)  # Expected Output:['banana', 'cherry']

# Example 3
list9 = [10, 20, 30, 40, 50]
list9.pop(3)  # we removing the number at index (3) which is number 40
print(list9)  # Expected Output:[10, 20, 30, 50]
