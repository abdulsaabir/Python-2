def remove_empty_string(strings):
    non_empty_strings = []

    for s in strings:
        if s.strip():  # Check if the string is not empty (after removing leading and trailing whitespace)
            non_empty_strings.append(s)

    return non_empty_strings

# Example usage:
list1 = ["Hello", "", "World", " ", "Python", ""]
result1 = remove_empty_string(list1)
print("Updated list:", result1)

list2 = ["This", "is", "a", "test", "", "program"]
result2 = remove_empty_string(list2)
print("Updated list:", result2)

list3 = ["1", "Two", "Three", "  ", "Four"]
result3 = remove_empty_string(list3)
print("Updated list:", result3)
