# Exercise 5: Iterate both lists simultaneously
#
# Given a two Python list. Write a program to iterate both lists simultaneously and display
# items from list1 in original order and items from list2 in reverse order.
#
# Given
#
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
#
# Expected output:
#
# 10 400
# 20 300
# 30 200
# 40 100

def iterateLists(list1: list[int], list2: list[int]):
    print("Using slicing: ")
    for item1, item2 in zip(list1, list2[::-1]):
        print(item1, item2)


def iterateLists2(list1: list[int], list2: list[int]):
    print("\nUsing revesed: ")
    for item1, item2 in zip(list1, reversed(list2)):
        print(item1, item2)

def main():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    (iterateLists(list1, list2))
    (iterateLists2(list1, list2))

main()
