# Exercise 2: Remove and add item in a list
#
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
from typing import Tuple, Any


# Given:
# list1 = [54, 44, 27, 79, 91, 41]
#
# Expected Output:
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]


items = [34, 54, 67, 89, 11, 43, 94]

# remove item at index 4
popped_item = items.pop(4)
print(f"List after removing element at index 4: {items}")

# add at index 2 popped out item
new_items = items.insert(2, popped_item)
print(f"List after adding element at index 2: {new_items}")

# add popped-out item at last index
new_items = items.append(popped_item)
print(f"List after adding element at index last: {new_items}")