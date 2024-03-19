# Exercise 4: Count the occurrence of each element from a list
#
# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to
# show the count of each element.
#
# Given:
#
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
#
# Expected Output:
#
# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}


def collectUniqueKeys(items:list[int]) -> list[int]:
    identities = []
    for item in items:
        if item not in identities:
            identities.append(item)
    return identities


def collectUniqueKeys2(items:list[int]) -> set[int]:
    return set(items)


def countItems(items:list[int]) -> dict[[int], [int]]:
    keys = collectUniqueKeys(items)
    # keys = set(items)
    items_dict = {}

    # fill dictionary with keys
    for item in keys:
        items_dict[item] = 0

    # count
    for item in items:
        items_dict[item] = items_dict[item] + 1

    return items_dict


def main():
    sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    print(collectUniqueKeys(sample_list))
    print(countItems(sample_list))


main()
