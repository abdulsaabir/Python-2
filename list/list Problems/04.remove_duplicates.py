def remove_duplicates(input_list):
    unique_list = []  # Create an empty list to store unique elements

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)  # Add items that are not already in the unique list

    return unique_list

# Example usage:
list1 = [1, 2, 2, 3, 4, 4, 5]
result1 = remove_duplicates(list1)
print("Updated list:", result1)

list2 = ["apple", "banana", "apple", "cherry"]
result2 = remove_duplicates(list2)
print("Updated list:", result2)

list3 = [5, 2, 7, 5, 1, 2, 9, 7]
result3 = remove_duplicates(list3)
print("Updated list:", result3)
