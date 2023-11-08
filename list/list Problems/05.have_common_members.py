def have_common_members(list1, list2):
    for item in list1:
        if item in list2:
            return True  # Return True if a common element is found

    return False  # Return False if no common element is found

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result1 = have_common_members(list1, list2)
print(result1)

list3 = ["apple", "banana", "cherry"]
list4 = ["date", "fig", "grape"]
result2 = have_common_members(list3, list4)
print(result2)
