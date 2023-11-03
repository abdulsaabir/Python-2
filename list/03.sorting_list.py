# Example 1: Sorting a List
my_list1 = [5, 2, 8, 1, 6]
my_list1.sort()
print("Example 1: Sorted list1 in ascending order:", my_list1)
# Expected Output: Example 1: Sorted list1 in ascending order: [1, 2, 5, 6, 8]

# Example 2: Sorting a List in Reverse Order
my_list2 = [5, 2, 8, 1, 6]
my_list2.sort(reverse=True)
print("Example 2: Sorted list2 in descending order:", my_list2)
# Expected Output: Example 2: Sorted list2 in descending order: [8, 6, 5, 2, 1]

# Example 3: Using Sorted Function
my_list3 = [5, 2, 8, 1, 6]
sorted_list = sorted(my_list3)
print("Example 3: Sorted list3 using the sorted function:", sorted_list)
# Expected Output: Example 3: Sorted list3 using the sorted function: [1, 2, 5, 6, 8]


# Here is brief explanation
"""
The difference between sort and reverse:

- sort() sorts the list in ascending order by default. 
  If you specify reverse=True, it sorts the list in descending order.

-reverse() reverses the order of the list without sorting it.

Example: [5, 2, 8, 1, 6] -> sort() -> [1, 2, 5, 6, 8]
Example: [5, 2, 8, 1, 6] -> sort(reverse=True) -> [8, 6, 5, 2, 1]
Example: [5, 2, 8, 1, 6] -> reverse() -> [6, 1, 8, 2, 5]


The difference between sorted and .sort:

sorted() is a built-in function that returns a new sorted list 
  without modifying the original list. It can be used with any iterable.

sort() is a method that sorts the original list in-place and returns None.
    the method of .sort it only can be used in list 


Example: [5, 2, 8, 1, 6] -> sorted() -> [1, 2, 5, 6, 8] (original list unchanged)
Example: [5, 2, 8, 1, 6] -> .sort() -> original list becomes [1, 2, 5, 6, 8]


"""