# Exercise 2: Remove and add item in a list
#
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
from typing import Tuple, Any, List


# Given:
# list1 = [54, 44, 27, 79, 91, 41]
#
# Expected Output:
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]


def removeItemAtPosition4(items: list[int]) -> tuple[int, list[int]]:
    copied_items = items.copy()
    popped_item = copied_items.pop(4)
    return popped_item, copied_items


def addItemAtPosition2(items: list[int], new_item: int) -> list[int]:
    copied_items = items.copy()
    copied_items.insert(2, new_item)
    return copied_items


def addItemAtPositionLast(items: list[int], new_item: int) -> list[int]:
    copied_items = items.copy()
    copied_items.append(new_item)
    return copied_items

### PROGRAM ####
# to remove global vars


def main():
    initial_items = [34, 54, 67, 89, 11, 43, 94]

    popped_item, new_items = removeItemAtPosition4(initial_items)
    print(f"List after removing element at index 4: {new_items}")

    new_items2 = addItemAtPosition2(new_items, popped_item)
    print(f"List after adding element at index 2: {new_items2}")

    new_items3 = addItemAtPositionLast(new_items2, popped_item)
    print(f"List after adding element at index last: {new_items3}")


main()
