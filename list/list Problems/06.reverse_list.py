# Solution 1 
def reverse_list(input_list):
    input_list.reverse()  # Use the 'reverse' method to reverse the list in place
    return input_list

# or you can use this solution 2 
def reverse_list(input_list):
    reversed_list = input_list[::-1]  # Use list slicing to reverse the order of elements
    return reversed_list



# Example usage:
original_list = [1, 2, 3, 4, 5]
result = reverse_list(original_list)
print("Reversed list:", result)
