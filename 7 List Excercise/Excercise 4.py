# Exercise 4: Concatenate two lists in the following order
#
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
# Expected output:
#
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


def ConcatenateTwoLists(list1: list[str], list2: list[str]) -> list[str]:
    list3 = []
    for index1 in range(len(list1)):
        for index2 in range(len(list2)):
            list3.append(list1[index1] + list2[index2])
    return list3


# alternative:
def ConcatenateTwoLists2(list1: list[str], list2: list[str]) -> list[str]:
    list3 = []
    for item1 in list1:
        for item2 in list2:
            list3.append(item1 + item2)
    return list3


# alternative using list comprehension:
# res = [x + y for x in list1 for y in list2]


def main():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    print(ConcatenateTwoLists(list1, list2))


main()
