# Exercise 9: Replace list’s item with new value if found
#
# You have given a Python list. Write a program to find value 20 in the list, and if it is present,
# replace it with 200. Only update the first occurrence of an item.
#
# Given:
#
# list1 = [5, 10, 15, 20, 25, 50, 20]
#
# Expected output:
#
# [5, 10, 15, 200, 25, 50, 20]


def replace20enumerate(numbers: list[int]) -> list[int]:
    print("Using enumerate():")
    for index, item in enumerate(numbers):
        if item == 20:
            numbers[index] = 200
            break
    return numbers

# In this example, enumerate() generates tuples containing the index and the corresponding item
# from the list my_list, and the loop iterates over these tuples. This allows you to access both
# the index and the item in each iteration of the loop.

def replace20index(numbers: list[int]) -> list[int]:
    print("\nUsing index():")
    numbers = [5, 10, 15, 20, 25, 50, 20]
    get_index = numbers.index(20)
    numbers[get_index] = 200
    return numbers

def main():
    # using enumerate().
    list1 = [5, 10, 15, 20, 25, 50, 20]
    print(replace20enumerate(list1))

    # using index().
    list1 = [5, 10, 15, 20, 25, 50, 20]
    print(replace20index(list1))

main()