# Exercise 6: Find the intersection (common) of two sets and remove those elements from the
# first set
#
# Given:
#
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
#
# Expected Output:
#
# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}


def findIntersection(set1:set[int], set2:set[int]) -> set[int]:
    intersected_set = set1.intersection(set2)
    return intersected_set


def removeCommonElements(set1:set[int], common_set: set[int]) -> set[int]:
    cleaned_set = set1.copy()

    for item in set1:
        if item in common_set:
            cleaned_set.remove(item)
    return cleaned_set


def main():
    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}

    common_set = findIntersection(first_set, second_set)
    print(f"Intersection is: {common_set}")

    print(f"First Set after removing common element: {removeCommonElements(first_set, common_set)}")



main()