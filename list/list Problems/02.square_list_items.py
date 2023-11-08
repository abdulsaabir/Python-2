def square_list_items(numbers):
    # Use a list comprehension to square each item in the input list
    squared_list = [x ** 2 for x in numbers]
    return squared_list

# Example usage:
list1 = [1, 2, 3, 4, 5]
result1 = square_list_items(list1)
print("Squared list:", result1)

list2 = [0, 10, 20, 30]
result2 = square_list_items(list2)
print("Squared list:", result2)
