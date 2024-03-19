# Exercise 5: Create a Python set such that it shows the element from both lists in a pair

# Given:
#
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
#
# Expected Output:
#
# Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}


def createPair(list1:list[int], list2:list[int]) -> set[(int, int)]:
    zipped = zip(list1, list2)
    # if "zipped": will return <zip object at 0x000001F708E73B00>, therefore give type as "set(zipped)"
    return set(zipped)



def main():
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    print(createPair(first_list, second_list))


main()