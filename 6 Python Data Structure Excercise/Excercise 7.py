# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all
# elements from that set.


# Given:
#
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}
#
# Expected Output:
#
# First set is subset of second set - True
# Second set is subset of First set -  False
#
# First set is Super set of second set -  False
# Second set is Super set of First set -  True
#
# First Set  set()
# Second Set  {67, 73, 43, 48, 83, 57, 29}


from typing import Tuple, Set


def isSubset(set1:set[int], set2:set[int]) -> tuple[bool, bool]:
    return set1.issubset(set2), set2.issubset(set1)


def isSuperset(set1:set[int], set2:set[int]) -> tuple[bool, bool]:
    return set1.issuperset(set2), set2.issuperset(set1)


def deleteItemsFromSet(set1:set[int], set2:set[int]) -> tuple[set[int], set[int]]:
    if set1.issubset(set2):
        set1.clear()

    if set2.issubset(set1):
        set2.clear()
    return set1, set2


def main():
    first_set = {27, 43, 34}
    second_set = {34, 93, 22, 27, 43, 53, 48}

    first_subset_second, second_subset_first = isSubset(first_set, second_set)
    print(f"First set is subset of second set: {first_subset_second}")
    print(f"Second set is subset of first set: {second_subset_first}")

    first_superset_second, second_superset_first = isSuperset(first_set, second_set)
    print(f"\nFirst set is superset of second set: {first_superset_second}")
    print(f"Second set is superset of first set: {second_superset_first}")

    deleteFirst, deleteSecond = deleteItemsFromSet(first_set, second_set)
    print("\nIf found, delete all elements from that set.")
    print(f"\tFirst set : {deleteFirst}")
    print(f"\tSecond set : {deleteSecond}")


main()